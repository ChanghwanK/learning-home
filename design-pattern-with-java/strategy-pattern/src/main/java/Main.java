import atm.Atm;
import pay.CardPay;
import pay.KakaoPay;
import pay.TossPay;

public class Main {
    public static void main(String...args) {
        Atm atm = new Atm(new KakaoPay());
        atm.pay();
    }
}
