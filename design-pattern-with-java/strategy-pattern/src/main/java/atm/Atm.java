package atm;

import pay.Pay;

public class Atm {

    private Pay pay;

    public Atm(Pay pay) {
        this.pay = pay;
    }

    public void pay() {
        pay.pay();
    }
}
