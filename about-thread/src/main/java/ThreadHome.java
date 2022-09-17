public class ThreadHome {

    public static void main(String... agrs) {
        var t1 = getForegroundThread();
        var t2 = getBackgroundThread();


        for (int i = 0; i < 10; i++) {
            t1.start();
            t2.start();
        }

        System.out.println("Main thread");

    }

    static Thread getForegroundThread() {
        return new Thread() {
            @Override
            public void run() {
                System.out.println("Foreground Thread");
            }
        };
    }

    static Thread getBackgroundThread() {
        return new Thread() {
            @Override
            public void run() {
                System.out.println("BackGround Thread");
            }
        };
    }
}
