

public class Test {
    public String secret = "MySecret";

    private void eval() {
        System.out.println("I am a test");
        String my_secret = "MySecret";
        String private_key = "-----BEGIN RSA PRIVATE KEY----- 123 -----END RSA PRIVATE KEY-----";
        String api_key = "1234567890abcdef1234567890abcdef";
        
        Test newtest = new Test();
        newtest.eval();
    }


}
