import com.authentix.core.AuthentixEngine;
import com.authentix.ui.AuthentixTab;
import com.authentix.core.model.*;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;

public class RenderAuthentixUi {
    public static void main(String[] args) throws Exception {
        System.setProperty("java.awt.headless", "false");
        AuthentixEngine engine = new AuthentixEngine();
        
        SwingUtilities.invokeAndWait(() -> {
            try {
                AuthentixTab tab = new AuthentixTab(engine);
                Component comp = tab.component();
                
                JFrame frame = new JFrame("Burp Suite Professional 2026.7 - AUTHENTIX Enterprise v2.1.0");
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                frame.setLayout(new BorderLayout());
                
                // Burp Suite Professional Top Tab Bar Styling
                JPanel burpHeader = new JPanel(new BorderLayout());
                burpHeader.setBackground(new Color(0x1B, 0x1E, 0x24));
                burpHeader.setBorder(BorderFactory.createMatteBorder(0, 0, 1, 0, new Color(0x2D, 0x32, 0x3F)));
                
                JPanel leftTabs = new JPanel(new FlowLayout(FlowLayout.LEFT, 0, 0));
                leftTabs.setOpaque(false);
                
                String[] tabs = {"Dashboard", "Target", "Proxy", "Intruder", "Repeater", "Collaborator", "Sequencer", "Decoder", "Comparer", "Extensions", "AUTHENTIX Enterprise"};
                for (String t : tabs) {
                    JLabel lbl = new JLabel(t);
                    lbl.setFont(new Font("Segoe UI", Font.BOLD, 12));
                    lbl.setBorder(BorderFactory.createEmptyBorder(8, 14, 8, 14));
                    if ("AUTHENTIX Enterprise".equals(t)) {
                        lbl.setForeground(new Color(0xFF, 0x88, 0x00));
                        lbl.setBackground(new Color(0x28, 0x2D, 0x3C));
                        lbl.setOpaque(true);
                        lbl.setBorder(BorderFactory.createCompoundBorder(
                            BorderFactory.createMatteBorder(0, 0, 2, 0, new Color(0xFF, 0x66, 0x00)),
                            BorderFactory.createEmptyBorder(8, 14, 6, 14)
                        ));
                    } else {
                        lbl.setForeground(new Color(0x9E, 0xA7, 0xB8));
                        lbl.setOpaque(false);
                    }
                    leftTabs.add(lbl);
                }
                
                JPanel rightInfo = new JPanel(new FlowLayout(FlowLayout.RIGHT, 14, 8));
                rightInfo.setOpaque(false);
                JLabel proj = new JLabel("Target: https://nimbusbank.internal  |  Montoya API 2026.7  |  Java 21  |  AUTHENTIX v2.1.0");
                proj.setFont(new Font("Segoe UI", Font.PLAIN, 11));
                proj.setForeground(new Color(0x6C, 0x76, 0x8A));
                rightInfo.add(proj);
                
                burpHeader.add(leftTabs, BorderLayout.WEST);
                burpHeader.add(rightInfo, BorderLayout.EAST);
                
                frame.add(burpHeader, BorderLayout.NORTH);
                frame.add(comp, BorderLayout.CENTER);
                frame.setSize(1600, 960);
                frame.setLocationRelativeTo(null);
                frame.setVisible(true);
                
                // Feed traffic in background thread, then trigger reevaluate
                new Thread(() -> {
                    try {
                        Thread.sleep(400);
                        feedTraffic(engine);
                        engine.reevaluate();
                        Thread.sleep(1200);
                        
                        SwingUtilities.invokeLater(() -> {
                            try {
                                BufferedImage img = new BufferedImage(frame.getWidth(), frame.getHeight(), BufferedImage.TYPE_INT_RGB);
                                Graphics2D g2 = img.createGraphics();
                                g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
                                g2.setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING, RenderingHints.VALUE_TEXT_ANTIALIAS_ON);
                                frame.paint(g2);
                                g2.dispose();
                                
                                File out = new File("assets/authentix_extension_dashboard.png");
                                ImageIO.write(img, "png", out);
                                System.out.println("SUCCESS: Generated " + out.getAbsolutePath() + " (" + out.length() + " bytes)");
                                frame.dispose();
                                System.exit(0);
                            } catch (Exception ex) {
                                ex.printStackTrace();
                                System.exit(1);
                            }
                        });
                    } catch (Exception e) {
                        e.printStackTrace();
                        System.exit(1);
                    }
                }).start();
                
            } catch (Exception e) {
                e.printStackTrace();
                System.exit(1);
            }
        });
    }
    
    static int exId = 100;
    private static void feedTraffic(AuthentixEngine engine) {
        long t = System.currentTimeMillis();
        
        // 1. Pre-auth fixation
        engine.ingest(ex("GET", "/dashboard", "actor-1", t += 100)
            .responseHeader("Set-Cookie", "sessionid=FIXEDSESSIONVALUE123; Path=/")
            .statusCode(200).build());
            
        // 2. Login using same cookie
        engine.ingest(ex("POST", "/login", "actor-1", t += 100)
            .requestHeader("Cookie", "sessionid=FIXEDSESSIONVALUE123")
            .requestBody("{\"username\":\"alice\",\"password\":\"hunter2\"}")
            .statusCode(200).responseBody("{\"status\":\"otp_required\"}").build());
            
        // 3. Brute force OTP window (6 attempts)
        for (int i = 0; i < 6; i++) {
            engine.ingest(ex("POST", "/otp/verify", "actor-1", t += 100)
                .requestHeader("Cookie", "sessionid=FIXEDSESSIONVALUE123")
                .requestBody("{\"code\":\"00000" + i + "\"}")
                .statusCode(401).responseBody("{\"error\":\"invalid code\"}").build());
        }
        
        // 4. Valid OTP verification (issued JWT with alg: none)
        String noneJwt = "eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiIxMDEiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWxpY2UifQ.";
        engine.ingest(ex("POST", "/otp/verify", "actor-1", t += 100)
            .requestHeader("Cookie", "sessionid=FIXEDSESSIONVALUE123")
            .requestBody("{\"code\":\"849201\"}")
            .statusCode(200).responseBody("{\"token\":\"" + noneJwt + "\"}").build());
            
        // 5. Cross-actor IDOR probe: Bob accessing Alice's resource
        engine.ingest(ex("GET", "/api/accounts/101", "actor-1", t += 100)
            .requestHeader("Cookie", "sessionid=FRESH_SESSION_ALICE")
            .statusCode(200).responseBody("{\"id\":101,\"balance\":99200.50,\"owner\":\"Alice\"}").build());
            
        engine.ingest(ex("GET", "/api/accounts/101", "actor-2", t += 100)
            .requestHeader("Cookie", "sessionid=FRESH_SESSION_BOB")
            .statusCode(200).responseBody("{\"id\":101,\"balance\":99200.50,\"owner\":\"Alice\"}").build());

        // 6. Forgot password token replay
        engine.ingest(ex("POST", "/forgot-password", "actor-1", t += 100)
            .requestBody("{\"email\":\"alice@nimbusbank.internal\"}")
            .statusCode(200).responseBody("{\"reset_token\":\"tok_reset_abc89712\"}").build());
            
        // 7. JS bundle with hardcoded secrets & client 2FA bypass
        engine.ingest(ex("GET", "/static/js/main.chunk.js", "actor-1", t += 100)
            .statusCode(200)
            .responseHeader("Content-Type", "application/javascript")
            .responseBody("const GOOGLE_API_KEY = \"AIzaSyD839-fakeExampleKey891024\";\nconst AWS_KEY = \"AKIAIOSFODNN7EXAMPLE\";\nconst bypass2FA = true;\nif (window.debugMode || localStorage.getItem('bypass2fa') === 'true') { return true; }").build());
    }
    
    private static HttpExchange.Builder ex(String method, String path, String actorTag, long ts) {
        exId++;
        return HttpExchange.builder()
            .exchangeId("ex-" + exId)
            .method(method)
            .url("https://nimbusbank.internal" + path)
            .host("nimbusbank.internal")
            .path(path)
            .requestHeader("X-Authentix-Actor", actorTag)
            .requestHeader("Host", "nimbusbank.internal")
            .timestampMillis(ts)
            .toolSource("Burp Proxy");
    }
}
