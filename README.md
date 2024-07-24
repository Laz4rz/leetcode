Literally **THE MOST** important thing when doing Leetcodes is: **MAKING SURE YOU UNDERSTOOD THE TASK**. I spent so much time thinking about non-existing problems, just because I misread or misunderstood something. For many of you English is not the first language. I know you know English well tho. I also understand English well. But understanding English and perfectly understanding the algorithmic task you are to implement, can someone mean two different things. Go slowly, it's just you and the task. You got it.

## Learning problems

Problems I want to describe in-depth, so that they will serve as examples, introducing terms, and approaches useful for all the other problems. 

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

How can we make it better? In general we know, that less than zero elements are bad, but we can't just remove them all. Sometimes they can be in the middle of good elements, and together make a maximum subarray.

Is there a way to make it smart? Turns out there it, we can simply cut the leading less than zero elements. Whenever our carried sum is below 0, we can be sure that it can be safely dropped, and either we hope that already found max is the real max, or the leftover elements will yield the real max. A good intuition on that: https://www.youtube.com/watch?v=5WZl3MMT0Eg where neetcode compares it to a sliding window — makes it nicer to understand.

```python
def maxSubArray(self, nums):
    # we get non-empty array, so we know max
    # has to be at least not smaller than the
    # first element
    maxSub = nums[0]
    currSum = 0

    # we make a single pass through the array
    for n in nums:
        # if our carried sum is smaller than 0
        # we dont need it, its not gonna do any
        # good to the leftover sums
        if currSum < 0:
            currSum = 0
        currSum += n
        maxSub = max(currSum, maxSub)
    
    return maxSub
```

This is quite beautiful. This approach is called Kadane's algorithm and it's time complexity is $O(n)$, since we make just a single pass over the elements.

---

#### 27. Remove Element (Easy)

So what do they mean by remove in-place? You may remember that certain operations in python can be done in place, that is, they will not return a new object that you need to assign to variable, instead they change the object you perform the operation on and it's kept under the same variable name. Probably the best Python example is the two ways to sort:

```python 
arr = [1, 3, 2]

# not in-place
# you need to assign new memory for a new variable
arrSorted = sorted(arr)

# in-place
# you operate on the same object in memory 
arr.sort()
```

So we are asked not to create a new array, for which we only append elements different than `val`. The usual way to do it is to move all elements not meeting the condition to the end of the array, and keeping track of the number of values meeting the condition. We can then return the array, and number of values meeting the condition. This way we cut off all the values we don't want. Imagine we don't want any 5s in our array:

```python
arr = [5, 2, 4, 1, 5, 6, 5]

remove5s(arr) # -> [2, 4, 1, 6, 5, 5, 5], 4
```

So the plan for this exercise is to just iterate over the examples, keeping track of current numbers meeting the condition, and swapping these numbers so that they occupy leading positions in the array:

```python
def removeElement(self, nums, val):
    n = len(nums)
    k = 0

    for i in range(n):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
```

We can't really do a better job. We are not taking any new memory, and the time complexity is just $O(n)$, as we only iterate once.

This class of problems is usually best solved with a two-pointer technique. We did just that, having `i` iterate over the whole array, and `k` keeping track of non-removed indexes. For a more in-depth explanation of two-pointer: https://leetcode.com/articles/two-pointer-technique.

---

#### 217. Contains Duplicate (Easy)

The brute force approach is to iterate with two for loops, and just compare all the numbers with each other. But we already know this is not a good solution. We also know it's time complexity thanks to the problem 53., we have nested for loops, so it's $O(n^2)$. 

```python
def containsDuplicate(self, nums):
    for num1 in nums:
        for num2 in nums:
            if num1 == num2:
                return True
    return False
```

So what can we do to make it better? One approach is to first sort the array (ie. with quicksort with time complexity $n\log n$) and then iterating just once, comparing subsequent elements. The total time complexity for this would be $O(n\log n + n)=O(n\log n)$ Remember? We talked in 53. that only the dominant terms matter in big O notation, that's why we only got the $n\log n$ part in final time complexity. 

##### Quicksort tangent

Learning how quicksort works is a typical journey in understanding any algorithm — you have to eyeball it, play with it, and magically it clicks. In general you pick the last element, sort the array in regard to this element so that it's placed in a correct spot, having smaller values to the left and greater values to the right. Then you recursively do that with the values on the left and values on the right, skipping the one element you placed correctly in the first function call. A good, slow animation is here: https://www.youtube.com/watch?v=Vtckgz38QHs&t=318s. 

Example of quicksort implementation is in `quicksort.py`. Tried on 100 random arrays of length 100, with ints between 0, and 100 it yields an average of 647.01 operations. Which is in the ballpark of expected $O(n \log n)$ as it would yield $700$ operations. For n=1000, average is 11090.93 — still not bad. Reminder that for worst case scenario, when the partitions quicksort creates while sorting, are heavily unbalanced, the complexity can grow up to $O(n^2)$.  

As we set to really make an example of these learning problems, we have to show the $O(n\log n)$ time complexity of quicksort. 

=== I'll get back to it ===

The third, and optimal way is to use a $O(1)$ accessible data structures — hash map or hash set. 

##### Hash map/set structure and how it's $O(1)$

When we use lists, we can't straight up access some value that's in it. We have to either know the index corresponding to it, or find it. It's because values are in no way related to the indexes. In hash structures like the map or set the values are in direct relation to the indexes, as the indexes are assigned with some kind of hash function. Heuristic is: $\text{WhatsMyAddress(someValue)}=\text{adressForThisValue}$. 

You of course try to make this function yield unique addresses. But you will fail, and sometimes these addresses will collide. Then you just have to iterate to the next free address. It may result in taking an address, that some other value would be given when put through the hashing. Well, too bad. Then this other value also has to iterate to the next free address. 

You may now wonder, if these colisions happen, how do we then get $O(1)$? Truth is — sometimes we don't. That's why the less collisions, the better. Cause whenever there is collision, we have to iterate, starting from the hash-that-would-be, to the hash that this value managed to get. 

```python
class HashSet:
    DEF_SIZE = 100

    def __init__(self, size: int = None):
        if size is None:
            size = self.DEF_SIZE
        self.arr = size * [None]
        self.size = size

    def hash(self, value: int):
        return value % self.size

    def put(self, value: int) -> None:
        hashed = self.hash(value)
        for i in range(hashed, self.size*2):
            try_hash = i % self.size
            if self.arr[try_hash] is None:
                self.arr[try_hash] = value
                print(f"Value {value} got key {try_hash}")
                return None
        print("No free hashes")

    def get(self, value: int) -> bool:
        hashed = self.hash(value)
        for i in range(hashed, self.size*2):
            try_hash = i % self.size
            if self.arr[try_hash] == value:
                return True
        return False
```

The above is also in `hashset.py`, together with some test cases. Please play with it, cause I may have skipped something, it's midnight. But the idea is there. 

##### Proper (and optimal) solution

Knowing all of this, but mostly about the existence, and complexity of accessing hashed data structures, we can finally write a proper solution. Got to admit that all this build up is going to fall off the cliff, because the pay-off is the simplest python code you've ever seen. But I believe, that unless I know how stuff works to the lowest level, I can't really make an informed decision of what to use, when and why. And I guess I want this FAANG job, so it's either fluent leetcodes or nothing for me.

```python
def containsDuplicate(self, nums):
    unique = set()
    n = len(nums)
    for num in nums:
        if num in unique:
            return True
        unique.add(num)
    return False
```

This does not really seem impressing right? But it is from a computational POV. We want from a potential $O(n^2)$ down to $O(n)$. Yeah, that's gonna impress this bored interviewing senior 10x engineer. Too bad it's an Easy problem. 

---

#### 2. Add Two Numbers (Medium)

We are asked to traverse two linked lists (they can have different lengths!), add the numbers, and return them in a linked list again. We know that due to the linked list nature, the numbers are placed there in reversed order. 

##### So what is a linked list?

I wont really go into the details here, because it's not really necessary. It's basically a matryoshka.

```python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
``` 

The class definition is pretty self-explanatory. You have a box with two holes. You put the value in one, and another box in the other hole.

##### Naive solution 

First solution that comes to mind is to just traverse both lists, add encountered values (scaling them by $10^i$, where $i$ is value's position in list), iterate over the accumulated value's digits (either as a string or calculating single digits), and put it in a new linked list. 

```python
def addTwoNumbers(self, l1, l2):
    acc = 0
    i = 0 

    while l1 is not None or l2 is not None:
        v1 = l1.val if l1 is not None else 0
        v2 = l2.val if l2 is not None else 0

        acc += (v1 * 10 ** i) + (v2 * 10 ** i)
        i += 1

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None

     ccs = str(acc)
     urr = ListNode(int(accs[0]), None)

     for el in accs[1:]:
        curr = ListNode(int(el), curr)

     return curr
``` 

The only hop here is that we have to handle the None tails of the lists we're traversing. Even though this solution is quite nice — time complexity is $O(n)$ — there are still some upgrades to be made, ie.: 

- addition digit by digit, not by building a whole number, as this could lead to an overflow for very long lists,  
- not using the int -> string conversion, cause even though it does not change the big O complexity, it adds an iteration

##### Optimal solution

If we are a little more smart — and want to deal with linked list back and forth pointers — we can do it in a single iteration. 

```python
def addTwoNumbers(self, l1, l2):
    # we need to initiate a dummy head so that
    # we can freely add new elements in the while loop
    # then we just drop this first node, and return
    # ones holding correct numbers
    ll_head = ListNode(0, None)
    tail = ll_head  
    carry = 0

    # why do we need the carry condition? the last
    # summation can yield a carry, so even though
    # we'll be finished with lists, we still have
    # to append carry
    while l1 is not None or l2 is not None or carry != 0:
        v1 = l1.val if l1 is not None else 0
        v2 = l2.val if l2 is not None else 0

        number = carry + v1 + v2
        digit = number % 10
        carry = number // 10
        
        # back and forth ll shenanigans that allow 
        # squishing it into a single loop
        # basically, we keep hold of the first element
        # because we need it for the return
        # and iteratively move the tail, so we can
        # add new elements as well
        node = ListNode(digit)
        tail.next = node
        tail = tail.next
        
        # thanks to this, we can skip checks like l1.next.next
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None

    r = ll_head.next
    return r
```

Funnily, my solution is basically the exact same solution that's available on the solutions page. Of course I am looking there for help when I'm really stuck, but this time I wrote it and was like "OH MY GOD ITS MY CODE THERE, ARE WE THE SAME PERSON!?". The comments should point you at what we are trying to do with all the nodes, you may need to ponder for a bit and it'll click. If not, then take the ListNode class and play with it. You'll get it.

---

169. Majority Element (Easy)

We are asked to find the most common element in a given array, we also know that this element will take more than $n/2$ of the total number of array elements. 

There pretty much is no bad approach. We can for example sort the array, and choose the middle element — we know that the majority element will be present at least $n/2$, so we are sure it will be in the middle no matter what after sorting. Thanks to 217. we know that the time complexity for the generally quickest sorting (quicksort) is $n \log n$. So the overall time complexity of this approach is also $n \log n$. Can we do better?

##### It's time optimal, but is it space optimal?

The second approach is to use a hash map as a counter, comparing the current most common element with updated counts of the current `nums` element. Thanks to hash structures $O(1)$ time complexity, we only pay the price of a single iteration over the array — $O(n)$.

```python
def majorityElement(self, nums):
    counter = {}
    majority = nums[0]

    for el in nums:
        if el in counter.keys():
            counter[el] += 1
        else:
            counter[el] = 1
        majority = el if counter[el] > counter[majority] else majority
    return majority
```

But what about space complexity? What even is space complexity? 

##### Space complexity

Space complexity is the big-O notation space taken by the algorithm. Depending on context you might be asked about the complexity with or without inputs. The convention is pretty bad, usually by space complexity people mean space taken without inputs. So if you have a function summing some array elements:

```python
def sum(arr):
    acc = 0
    for el in arr:
        acc += el
    return acc
```

The space complexity will be $O(1)$, cause you only initialized an single value variable `acc`. But if you want to go strict-math-gestapo, then it's actually space complexity and auxiliary complexity.

- Space complexity: total space taken by the inputs and additional variables
- Auxiliary complexity: only space taken by additional variables

So for the `sum` function the strict space complexity would be $O(n + 1) = O(n)$, as you have an array of inputs of length $n$ and a single value `acc`, but for big-O only the dominant terms matter (again look at 217. if are unsure why). Auxiliary space would be $O(1)$, cause we only look at the additional variable, so `acc` in this example.

As for our `majorityElement` function, the space complexity is $O(n + 2n + 1) = O(n)$, where the terms are respectively: inputs, dictionary ($n$ keys and $n$ items), and `majority`. As we are not concerned with constant factors in big-O, the whole thing shortens to just $O(n)$. The auxiliary complexity in this example is the same as space complexity cause $O(2n + 1) = O(n)$.

Here I guess I'll be using the space complexity term to talk about auxiliary complexity. In the followup to this leetcode we are asked to bring the "space complexity" down to $O(1)$, but we wouldn't be able to do that to THE space complexity, meaning inputs + additional variables. So they got to be asking about THE auxiliary complexity. Due to different sources using space complexity name instead of auxiliary, we will stick to it so we agree with the common convention. We don't have to be that strict. We are not mathematicians.

##### Very optimal solution

Turns out we can write a solution with time complexity $O(n)$ and space complexity $O(1)$ — doesn't it sound amazing (Probably no, if you have a happy grass-touching life)!?

Moore's voting algorithm, is literally made for finding the majority element. Think of it as growing in power when more of the same elements are found or losing hp points when you encounter a different element. We know that the majority element will have at least $n/2 + 1$ times. So not even all it's enemies (other elements) together (counted) can bring it down ($n/2 + 1 > \sum\text{other}$). 

```python
def majorityElement(self, nums):
    majority = 0
    counter = 0

    for el in nums:
        if el == majority:
            counter += 1
        else:
            counter -= 1
        
        if counter < 0:
            majority = el
            counter = 0
    return majority
```

There you have it. Now you not only recognize, but also understand the inner workings of the most important terms in all leetcodes: quicksort, hash structures, time complexity, and space complexity. You also know how to approach, and iterate on your solutions, aiming at the most optimized space/time complexities. 

---

#### 26. Remove duplicates (Easy)

Now is the time to put all of the above into practice. There is no reason for us not to one-shot the optimal solution for this problem, it's literally problem 27. all over again. 

We know that it's sorted, we know what in-place means, we know that for problems like this two-pointer technique could be useful. So let's just adapt the 27. solution, check complexities to see whether there is place for any more optimization, and call it a day.

```python
def removeDuplicates(self, nums):
    k = 1
    prev = nums[0]

    for el in nums[1:]:
        if prev != el:
            nums[k] = el
            k += 1
            prev = el
    return k
```

Give yourself a quiz now. Time complexity? Space complexity?

- Time complexity: $O(n)$ as we only ride a single iteration over inputs in the for loop
- Space complexity: $O(1)$, cause we only hold single valued variables, not growing with input size

There you have it. We are so good now, we can start doing these "ummm yeah, I haven't seen this problem, but I can try..." and the proceed to build an optimal solution scenes that the recruiting managers love so much. 

---

There you have it. Enjoy the grind. Crush like 100 more problems and apply for the job you always wanted.
