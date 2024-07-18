Literally **THE MOST** important thing in doing Leetcodes is: **MAKING SURE YOU UNDERSTOOD THE TASK**. I spent so much time thinking about non-existing problems, just because I misread or misunderstood something. For many of you English is not the first language. I know you know English well tho. I also understand English well. But understanding English and perfectly understanding the algorithmic task you are to implement, can someone mean two different things. Go slowly, it's just you and the task. You got it.

## Learning problems

Problems I want to describe in-depth, so that they will serve as examples for all the other ones. 

#### 9. Palindrome Number (Easy)

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

---

#### 53. Maximum Subarray (Medium)

**Rewritten instruction**: Find the maximum sum of consecutive elements of the array.

##### Solution(s)

The first, obvious and with zero intuition, approach is to just double loop over the array elements. This works, but it's not good. Wanna guess the time complexity? You're right: $O(n^2)$.

**Why? Quicky on double loop time complexity:**

For each of the outer loops iteration $i$, we get $n-i$ inner loop iterations. Therefore the total of all iterations is:

$$S = (n-1) + (n-2) + (n-3) +...+1$$

Back to primary school: how to calculate the sum of arithmetic progressions? In general the arithmetic progression is something that starts at some $a_0$, has constant additive element $d$, and is bounded by the number of elements $n$ (it turns into arithmetic series when the number of elements is not bounded: $n \to \infty$). 

**Derivation of the arithmetic progression sum formula:**

We will an example of the progression in a normal form, and reversed. 

$$S_f = 1 + 2 + ... + (n-1) + n$$

$$S_r = n + (n-1) + ... + 2 + 1$$

Now eyeball it. First term on both, second term on both... 

$$S_f + S_r = (n+1) + (n+1) + (n+1)... = 2S$$

Yeaaah, it's all coming together. How many terms is there: $n$. Each term is: $n+1$. So it's all just:

$$2S = n(n+1)$$

$$S = \frac{n(n + 1)}{2}$$

Now, being absolutely sure, we understand how many iteration we have down to atomic level, we can get back to how we come up with complexity $O(n^2)$.

We calculate the big-O complexity, by finding the dominating factor as $n$ grows towards infinity. If you ever calculated series sums. It's the same principle. You look for whatever term that outgrows others by orders of magnitude as $n$ grows. In this case, when we multiply the upper term:

$$S = \frac{n^2+n}{2}$$

Quadratic function grows faster than the linear one. Graphical way to understand why $n^2$ dominates for bigger $n$. You'd literally have to take something like $n=\frac{1}{3}$, for n to be bigger. 

![alt text](images/complexity_n2_n.png)

Now, we can finally see the naive and bad solution, understanding why it's naive and bad. 

```python
def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    top = float("-inf")
    acc = 0
    n = len(nums)

    for i in range(n):
        acc = nums[i]
        if acc > top:
            top = acc
        for j in range(i+1, n):
            acc += nums[j]
            if acc > top:
                top = acc
    return top
```

Now remember the intuition I wrote above. That's why reading the instruction **very** slowly is so important. We do not have to iterate so many times.

