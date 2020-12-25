import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Random;

public class LotteryGames {

    public static void main(String[] args) {
        LotteryGames lg = new LotteryGames();
        lg.powerBall();
        lg.lotto();
        lg.dailyLotto();
        lg.ukLunchAndTea();
        lg.allORNothing();
    }

    public void powerBall() {
        // 5 numbers between 1 and 50 and an extra number/the powerball from 1 to 20
        System.out.println("Your next powerball numbers:   Play with R5");
        severalLottoGames(5, 1,50, true);
    }

    public void lotto(){
        // Choose 6 numbers between 1 and 52.
        System.out.println("\nYour next lotto numbers:      Play with R5");
        severalLottoGames(6, 1, 52, false);
    }

    public void dailyLotto(){
        System.out.println("\nYour next daily lotto numbers:    Play with R3");
        severalLottoGames(5, 1, 36, false);
    }

    public void ukLunchAndTea(){
        System.out.println("\nYour next uk49 numbers:   Play with 1, 2, 3 rand");
        severalLottoGames(3, 1,49, false);
        severalLottoGames(3, 1,49, false);
        severalLottoGames(3, 1,49, false);
        severalLottoGames(3, 1,49, false);
        severalLottoGames(3, 1,49, false);
    }

    public void allORNothing(){
        System.out.println("\nYour next All Or Nothing numbers: 8 LINES - R8");
        severalLottoGames(3, 1, 24, false);
        severalLottoGames(3, 1, 24, false);

        severalLottoGames(3, 10, 24, false);
        severalLottoGames(3, 10, 24, false);

        System.out.println("Change the last numbers. Morning release");

        System.out.println("Change the first numbers. Day session");

        System.out.println("change the middle numbers. Evening session.");

        System.out.println("Leave as is. Night session. RUN TWICE");

        //System.out.println();
        // Six numbers to win R101 with R1
        //severalLottoGames(6, 1,24, false);
        // Six numbers to win R301 with R1
       // severalLottoGames(7, 1,24, false);
        // Six numbers to win R901 with R1
        //severalLottoGames(8, 1,24, false);
    }

    public void severalLottoGames(int numNumbers, int min, int max, boolean isExtraNum){

        int [] nums = new int[numNumbers];
        Random rd = new Random();

        for (int i = 0; i < numNumbers; i++) {
//            int num = rd.nextInt(max) + 1;
            int num = rd.nextInt((max - min) + 1) + min;

            if (i > 0)
                for (int j = 0; j < i; j++) {

                    if (num == nums[j])
                        num = rd.nextInt((max - min) + 1) + min;
                }
            nums[i] = num;
        }

        Arrays.sort(nums);

        // The powerball
        int extraNum = 0;
        if (isExtraNum)
            extraNum = rd.nextInt(20) + 1;

        StringBuilder play = new StringBuilder();
        for (int i = 0; i < nums.length; i++)
            play.append(nums[i] + " ");

        if (isExtraNum)
            play.append("+ " + extraNum);

        System.out.println(play.toString());
    }


}
