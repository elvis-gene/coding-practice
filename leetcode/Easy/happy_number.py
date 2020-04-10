class Solution:
    def isHappy(self, n: int) -> bool:

        # HashSet<Integer> set = new HashSet<Integer>();
        # while(!set.contains(n)){
        #     set.add(n);
        #     int sum = 0;
        #     while(n>0){
        #         int digit = n%10;
        #         sum+=digit*digit;
        #         n/=10;
        #     }
        #     n=sum;
        # }
        # return n==1;

        if n > 0:
            list_set = set()
            while n not in list_set:  # At the end, 1 will always be equal to one
                list_set.add(n)
                new_num = 0

                # After the square of the last digit is added to the sum,
                # the result of n = n/10 will be zero
                while n > 0:
                    digit = n % 10
                    new_num = new_num + digit**2
                    n = n/10
                n = new_num

            return n == 1
