Literally **THE MOST** important thing in doing Leetcodes is: **MAKING SURE YOU UNDERSTOOD THE TASK**. I spent so much time thinking about non-existing problems, just because I misread or misunderstood something. For many of you English is not the first language. I know you know English well tho. I also understand English well. But understanding English and perfectly understanding the algorithmic task you are to implement, can someone mean two different things. Go slowly, it's just you and the task. You got it.

#### 9. Palindrome Number

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        # naive approach
        # we reverse the whole number and compare to the original
        # reversing is done, by cutting off the last digit of the
        # input, we do that in a loop:
        # 1. cut last number by modulo
        # 2. add it to the reverse, multiplying previous by 10,
        #    cause each new digit is a new decimal place
        # 3. complete division by 10 on original number, to cut
        #    the digit
        reverse = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp = temp // 10

        return reverse == x

    def isPalindrome2(self, x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        # optimal approach
        # reverse only the last half of the numbers, and compare
        # with the first half, skip the middle number if exists
        # we terminate the while if reverse is bigger than reverse
        # it takes a minute to be mentally sure its a good condition
        # but it is, and thinking about it is easier than writing it
        # down shortly
        # we need to add additional return for not even numbers, cause
        # above termination mechanism will eat the middle number

        reverse = 0
        original = x

        while x > reverse:
            reverse = reverse * 10 + x % 10
            x = x // 10

        return x == reverse or x == (reverse // 10) # second is for not even
```
