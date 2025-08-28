# --- IMPORTANT: Before running, make sure you've installed gTTS, pydub, and FFmpeg! ---

import os
from gtts import gTTS
from pydub import AudioSegment

# --- PART 1: Your Document Text & Settings ---

# 1. PASTE YOUR ENTIRE DOCUMENT TEXT HERE!
#    This variable will hold all the pattern explanations you provided.
document_text = """
Sliding Window Pattern
Hey there! Imagine you have a long, long train with many cars, and each car has a number on it. You want to find something special about a group of these cars, say, 3 cars in a row.

Now, instead of looking at every single possible group of 3 cars (which would take forever if the train is super long!), you can use a cool trick called the Sliding Window Pattern.

Here's how it works:

The Window: Imagine you have a special "window" that can only show you 3 train cars at a time.

Slide, Don't Jump:
First, you put your window over the first 3 cars (Car 1, Car 2, Car 3). You do your special calculation on them (maybe add up their numbers, or find the biggest number).
Instead of moving your window all the way to Car 4, Car 5, Car 6, you just **slide** your window one car over to the right.
Now your window shows Car 2, Car 3, Car 4. See how Car 1 "left" the window and Car 4 "entered"?
You do your special calculation again.

Keep Sliding: You keep sliding your window one car to the right, always keeping it 3 cars wide, until you've looked at all the cars on the train.

Why is this so cool?

* It's super-fast! Think about it: if you have a train with 100 cars and you want to look at groups of 3, you'd only do about 98 calculations with the sliding window. If you had to look at every single combination, it would be way more work!
* It's smart! You're reusing information. When you slide the window from (Car 1, Car 2, Car 3) to (Car 2, Car 3, Car 4), you don't need to re-examine Car 2 and Car 3. You only need to deal with Car 1 leaving and Car 4 entering.

Let's try an example:

Imagine you have a list of numbers: [1, 5, 2, 7, 8, 3]
And you want to find the group of 3 numbers that adds up to the biggest sum.

* Window 1: [1, 5, 2] -> Sum = 8
* Slide! Remove 1, add 7.
* Window 2: [5, 2, 7] -> Sum = 14
* Slide! Remove 5, add 8.
* Window 3: [2, 7, 8] -> Sum = 17
* Slide! Remove 2, add 3.
* Window 4: [7, 8, 3] -> Sum = 18

So, the group [7, 8, 3] has the biggest sum (18)!

In programming, we use this for things like:

* Finding the longest sequence of something.
* Calculating averages over a certain period.
* Checking if a part of a message has a certain pattern.

---
Two Pointers Pattern
Imagine you have a super long line of your friends, and each friend has a number on their shirt. You want to find something special about two friends in that line.

Now, instead of picking one friend, then picking another friend, and doing that over and over again, you can use a cool trick called the Two Pointers Pattern.

Here's how it works:

Two "Fingers" (Pointers): Imagine you have two fingers, or two special markers. You place one marker (let's call it "Left Pointer") at the very beginning of your line of friends. You place the other marker (let's call it "Right Pointer") at the very end of the line.

Moving Towards Each Other (or in the Same Direction):
You look at the two friends your pointers are on. You do some kind of check or calculation with their numbers.
Based on what you find, you decide to move one of your pointers.
If the numbers don't match what you're looking for, maybe you move the "Left Pointer" one step to the right.
Or maybe you move the "Right Pointer" one step to the left.
Sometimes, both pointers move in the same direction, but usually, they move towards each other!

Keep Going Until They Meet (or Cross): You keep moving your pointers, checking the friends they point to, and deciding which pointer to move, until:
The "Left Pointer" crosses the "Right Pointer" (meaning they've checked all possible pairs).
Or the pointers meet on the same friend.
Or you find exactly what you're looking for!

Why is this so cool?

* Super Efficient! Instead of checking every single possible pair of friends (which can be a huge number if you have a lot of friends!), this method lets you find things much, much faster. It's like having a superpower for searching!
* Simple to Understand! Once you get the idea of two markers moving, it becomes very clear what's happening.

Let's try an example:

Imagine you have a list of numbers that are already sorted from smallest to largest: [1, 3, 5, 8, 9, 11] And you want to find two numbers that add up to 14.

* Left Pointer (L): Starts at 1 (the first number).
* Right Pointer (R): Starts at 11 (the last number).

Let's play:

1.  L points to 1, R points to 11.
    * Sum = 1 + 11 = 12.
    * 12 is less than 14. This means we need a bigger sum. To get a bigger sum, we need to increase the smaller number. So, move the Left Pointer to the right!
    * L moves to 3.

2.  L points to 3, R points to 11.
    * Sum = 3 + 11 = 14.
    * Aha! We found it! 3 and 11 add up to 14. We can stop here.

See how quickly we found it? If we didn't use two pointers, we might have to try 1+3, 1+5, 1+8, etc., which takes a lot longer!

In programming, we use this for things like:

* Finding pairs of numbers that add up to a target.
* Reversing a list or array.
* Checking if a word reads the same forwards and backward (like "madam").
* Finding duplicates or unique items in a list.

---
Fast and Slow Pointer Pattern
Hey there! Imagine you have a race track, and you have two friends who are going to run on it:

1.  "Slowpoke" (The Slow Pointer): This friend runs at a regular, steady pace, taking one step at a time.
2.  "Zoomy" (The Fast Pointer): This friend runs much faster, taking two steps at a time (or maybe even more!).

This is the basic idea behind the **Fast and Slow Pointer Pattern** in programming! You have two "pointers" (which are like markers or arrows pointing to something in your computer's memory), and one moves faster than the other.

Why is this so cool and useful?

It's especially good for solving problems where things might be connected in a circle, or when you need to find the middle of something without knowing how long it is.

Let's use an example: The Loopy Train

Imagine you have a train, but it's a very strange train. Instead of going straight to the end, sometimes a train car is connected back to an earlier car, making a loop (a circle)!

Car 1 -> Car 2 -> Car 3 -> Car 4 -> Car 5 -> Car 3 (Uh oh, a loop!)

How can you tell if your train has a loop, and where the loop starts, if you can only look at one car at a time?

This is where Slowpoke and Zoomy come in!

* Start: Both Slowpoke and Zoomy start at Car 1.
* Run!
    * Slowpoke moves one car forward at a time.
    * Zoomy moves two cars forward at a time.

Let's trace their steps:

* Start: Slowpoke (Car 1), Zoomy (Car 1)
* Step 1: Slowpoke (Car 2), Zoomy (Car 3)
* Step 2: Slowpoke (Car 3), Zoomy (Car 5)
* Step 3: Slowpoke (Car 4), Zoomy (Car 3) <-- Aha!

Notice something amazing? Slowpoke and Zoomy are now on the **same car** (Car 3)!

This can only happen if there's a loop! If the train just went straight, Zoomy would always be ahead of Slowpoke and they would never meet (unless Zoomy reached the end of the train first). But because Zoomy is faster, if there's a circle, Zoomy will eventually "lap" Slowpoke and catch up to them inside the loop.

What if they meet?

When they meet, it tells you there's a loop. You can even do more cool things:

* Find where the loop starts: If they meet, you can reset one pointer (say, Slowpoke) back to the beginning (Car 1). Then, move both Slowpoke and Zoomy one step at a time until they meet again. Where they meet that second time is the very beginning of the loop! (In our example, if Slowpoke went back to Car 1 and Zoomy stayed at Car 3, and both moved one step at a time, they would meet at Car 3.)

In programming, we use this for things like:

* Detecting cycles (loops) in data structures: Just like our loopy train example, this is super common.
* Finding the middle element of a list: If Zoomy runs twice as fast, when Zoomy reaches the end, Slowpoke will be exactly in the middle!
* Finding where a cycle starts.

---
Merge Interval Pattern
Hey there! Imagine you have a bunch of tasks you need to do, and each task has a "start time" and an "end time." For example:

* Task A: Starts at 9:00 AM, Ends at 10:00 AM (written as [9, 10])
* Task B: Starts at 9:30 AM, Ends at 11:00 AM (written as [9.5, 11])
* Task C: Starts at 12:00 PM, Ends at 1:00 PM (written as [12, 13])
* Task D: Starts at 10:30 AM, Ends at 12:30 PM (written as [10.5, 12.5])

Notice how Task A and Task B overlap? And Task D overlaps with where Task B ends and Task C begins?

The **Merge Interval Pattern** is a cool way to combine any tasks (or "intervals") that overlap into one bigger, combined task. It's like finding the total time you'll be busy, without counting overlapping parts multiple times.

Think of it like this:

You have a messy calendar with appointments that might be stacked on top of each other. You want to clean it up so you have the fewest possible "busy blocks."

How it works (the "recipe"):

1.  Get Organized First! (Sort): The most important first step is to sort all your tasks (intervals) by their start time. This makes sure you're always looking at tasks in the correct order.

    Let's reorder our example tasks by start time:
    * Task A: [9, 10]
    * Task B: [9.5, 11]
    * Task D: [10.5, 12.5]
    * Task C: [12, 13]

2.  Start Your Merged List: Grab the very first task (after sorting) and make it the first "merged" task in your new, clean calendar.

    * Merged List: [ [9, 10] ] (This is our current combined task)

3.  Look at the Next Task & Decide: Now, go through the rest of the sorted tasks, one by one. For each "next task," you ask yourself:

    * Does it overlap with my current combined task?
        * How to check: Does the "next task's" start time happen before or at the same time as the "current combined task's" end time?

    * If YES (they overlap):
        * Good! You can make your "current combined task" bigger. You update its "end time" to be the maximum of its current end time and the "next task's" end time.
        * Example: Current [9, 10], Next [9.5, 11]
            * 9.5 (next start) is before 10 (current end), so they overlap!
            * New current combined task becomes [9, max(10, 11)] which is [9, 11].
            * Merged List: [ [9, 11] ]

    * If NO (they don't overlap):
        * This means your "current combined task" is finished! It's as big as it can get. Add it to your final list of merged tasks.
        * Then, the "next task" becomes your brand new "current combined task," and you start comparing future tasks to it.

Let's trace our example:

* Sorted Tasks: [9, 10], [9.5, 11], [10.5, 12.5], [12, 13]
* Final Merged List: []
* Current Merged Task: null

1.  Process [9, 10]:
    * No Current Merged Task yet. So, this becomes our Current Merged Task.
    * Current Merged Task = [9, 10]

2.  Process [9.5, 11]:
    * Does [9.5, 11] overlap with [9, 10]? Yes, 9.5 is less than 10.
    * Merge them: Current Merged Task = [9, max(10, 11)] = [9, 11]

3.  Process [10.5, 12.5]:
    * Does [10.5, 12.5] overlap with [9, 11]? Yes, 10.5 is less than 11.
    * Merge them: Current Merged Task = [9, max(11, 12.5)] = [9, 12.5]

4.  Process [12, 13]:
    * Does [12, 13] overlap with [9, 12.5]? Yes, 12 is less than 12.5.
    * Merge them: Current Merged Task = [9, max(12.5, 13)] = [9, 13]

5.  Finished! We've processed all tasks. Add the very last Current Merged Task to our Final Merged List.

    * Final Merged List: [ [9, 13] ]

So, all those messy tasks [9, 10], [9.5, 11], [10.5, 12.5], [12, 13] actually just combine into one big busy block from 9:00 AM to 1:00 PM!

Why is this pattern useful in programming?

* Scheduling: Like our calendar example, combining meeting times or resource bookings.
* Time Management Apps: Calculating total active time.
* Genetics/Biology: Finding overlapping gene segments.
* Geometry: Merging overlapping line segments or ranges.

---
Cyclic Sort Pattern
Hey there! Imagine you have a special drawer for each of your favorite toys, numbered 1, 2, 3, and so on. So, Toy #1 should go in Drawer #1, Toy #2 in Drawer #2, and so on.

But one day, your mischievous little sibling mixes up all your toys and shoves them into the drawers randomly! Now, Toy #3 might be in Drawer #1, and Toy #1 might be in Drawer #5!

The **Cyclic Sort Pattern** is like a super-smart way to put all those toys back into their correct drawers, super efficiently, without needing extra space.

The Big Idea:
The main idea is that if you have a list of numbers from 1 to N (or 0 to N-1), each number belongs in a specific spot. For example, the number 5 belongs in the 5th spot (or index 4 if we start counting from 0).

How it Works (The "Toy Sorting Machine"):

Let's say your drawers (which are like "slots" in programming) are numbered 1 to 5, and you have toys numbered 1 to 5, but they're all messed up:

[3, 5, 1, 2, 4] (Meaning: Drawer 1 has Toy 3, Drawer 2 has Toy 5, etc.)

Here's how our "Cyclic Sort" machine works:

1.  Start at the First Drawer (Index 0): Look at what's in Drawer 1 (which is index 0 in programming).
    * Right now, Toy #3 is in Drawer 1.

2.  Is it in the Right Place?
    * Toy #3 should be in Drawer 3 (index 2).
    * Is it there? No, it's in Drawer 1.

3.  Swap It to Its Home!
    * Since Toy #3 belongs in Drawer 3, we're going to **swap** Toy #3 with whatever is currently in Drawer 3.
    * What's in Drawer 3 (index 2) right now? Toy #1.
    * So, we swap Toy #3 and Toy #1!

    Your drawers now look like this: [1, 5, 3, 2, 4] (Toy #1 is now in Drawer 1, Toy #5 in Drawer 2, Toy #3 in Drawer 3...)

4.  Don't Move Yet! (Check Again at the Same Drawer):
    * Now, look at Drawer 1 **again**. What's in there **now**? It's Toy #1!
    * Is Toy #1 in the right place? Yes, Toy #1 belongs in Drawer 1!
    * Great! Since Drawer 1 is now correct, we can move to the **next** drawer.

5.  Move to the Next Drawer (Index 1): Look at Drawer 2.
    * What's in Drawer 2? Toy #5.
    * Is Toy #5 in the right place? No, Toy #5 should be in Drawer 5 (index 4).

6.  Swap It to Its Home!
    * Swap Toy #5 (from Drawer 2) with whatever is in Drawer 5 (Toy #4).

    Your drawers now look like this: [1, 4, 3, 2, 5] (Toy #1 in Drawer 1, Toy #4 in Drawer 2, Toy #3 in Drawer 3, Toy #2 in Drawer 4, Toy #5 in Drawer 5)

7.  Check Again at the Same Drawer:
    * Look at Drawer 2 **again**. What's in there **now**? Toy #4.
    * Is Toy #4 in the right place? No, Toy #4 should be in Drawer 4 (index 3).

8.  Swap It to Its Home!
    * Swap Toy #4 (from Drawer 2) with whatever is in Drawer 4 (Toy #2).

    Your drawers now look like this: [1, 2, 3, 4, 5] (Toy #1 in Drawer 1, Toy #2 in Drawer 2, Toy #3 in Drawer 3, Toy #4 in Drawer 4, Toy #5 in Drawer 5)

9.  Check Again:
    * Look at Drawer 2 **again**. What's in there? Toy #2.
    * Is Toy #2 in the right place? Yes!
    * Great! Move to the next drawer (Drawer 3).

... and you continue this process until you've checked all the drawers. Because you only move to the next drawer once the current drawer is correct, you ensure everything ends up in its proper place.

Why is this pattern super useful?

It's great when you have a list of numbers that are almost sorted, or when you know the range of numbers (like 1 to N) and you want to:

* Find missing numbers: If a drawer is empty (or has the wrong toy), you know a number is missing.
* Find duplicate numbers: If you try to put a toy into a drawer and that drawer **already** has the correct toy, then the toy you just tried to put there must be a duplicate!
* Put numbers in their correct positions without using any extra memory.

---
In place reversal of linked lists
Hey there! Imagine you have a super special train. But it's not like a regular train where all the cars are just connected in a line. In *this* train, each car only knows which car is **next** in line. It's like a treasure hunt where each clue (train car) tells you exactly where the *next* clue is!

So, you have something like:
`Car 1` ➡️ `Car 2` ➡️ `Car 3` ➡️ `Car 4` ➡️ `End of Train`

This is what we call a "Linked List" in programming. Each "Car" is called a "Node," and the arrow is its "next" pointer.

Now, your challenge is to make this train go *backward*! You want it to look like this:
`Car 4` ➡️ `Car 3` ➡️ `Car 2` ➡️ `Car 1` ➡️ `End of Train`

But there's a big rule: You can't just build a whole *new* train. You have to do this "**in-place**." That means you can only use the cars you already have, and you can only change *their* connections. You can't bring in extra cars or a separate track to sort them out. It's like re-hooking the cars one by one directly on the main track.

The "Three Hands" Magic (Our Pointers):

To do this trick, you need three special "hands" (in programming, we call these "**pointers**") to help you keep track of things:

1.  **`Previous` Hand:** This hand points to the car that you've *already* finished hooking up in the new backward direction. At the very beginning, nothing is hooked up backward yet, so this hand points to "nothing" (which we call `null`).
2.  **`Current` Hand:** This hand points to the car you are *currently* working on – the one you're about to flip its connection. At the start, it points to `Car 1`.
3.  **`Next` Hand:** This is super important! Before you change the `Current` car's connection, you need to quickly look ahead with this hand to see which car is *after* the `Current` car. Otherwise, you'll lose the rest of your train!

Let's walk through it step-by-step with our train: `1` ➡️ `2` ➡️ `3` ➡️ `4`

* **Start:**
    * `Previous` = `null`
    * `Current` = `Car 1`
    * `Next` = (we'll find this in step 1)

**Round 1 (Working on `Car 1`):**

1.  **`Next` Hand looks ahead:** The `Next` car after `Current` (Car 1) is `Car 2`. So, `Next` = `Car 2`.
2.  **Flip `Current`'s connection:** Make `Current` (Car 1) point *backward* to what `Previous` was pointing to (`null`).
    * Now: `null` ⬅️ `Car 1`
3.  **Slide `Previous` hand:** Move `Previous` to where `Current` just was. So, `Previous` = `Car 1`.
4.  **Slide `Current` hand:** Move `Current` to where `Next` was pointing. So, `Current` = `Car 2`.

* **After Round 1:**
    * `Previous` = `Car 1`
    * `Current` = `Car 2`
    * `Next` = (still `Car 2` from previous step, but we'll update it for the next round)
    * Train looks like: `null` ⬅️ `1`   `2` ➡️ `3` ➡️ `4` (still connected to 3)

**Round 2 (Working on `Car 2`):**

1.  **`Next` Hand looks ahead:** The `Next` car after `Current` (Car 2) is `Car 3`. So, `Next` = `Car 3`.
2.  **Flip `Current`'s connection:** Make `Current` (Car 2) point *backward* to what `Previous` was pointing to (`Car 1`).
    * Now: `Car 1` ⬅️ `Car 2`
3.  **Slide `Previous` hand:** Move `Previous` to where `Current` just was. So, `Previous` = `Car 2`.
4.  **Slide `Current` hand:** Move `Current` to where `Next` was pointing. So, `Current` = `Car 3`.

* **After Round 2:**
    * `Previous` = `Car 2`
    * `Current` = `Car 3`
    * `Next` = (still `Car 3` from previous step)
    * Train looks like: `null` ⬅️ `1` ⬅️ `2`   `3` ➡️ `4` (still connected to 4)

**Round 3 (Working on `Car 3`):**

1.  **`Next` Hand looks ahead:** The `Next` car after `Current` (Car 3) is `Car 4`. So, `Next` = `Car 4`.
2.  **Flip `Current`'s connection:** Make `Current` (Car 3) point *backward* to what `Previous` was pointing to (`Car 2`).
    * Now: `Car 2` ⬅️ `Car 3`
3.  **Slide `Previous` hand:** Move `Previous` to where `Current` just was. So, `Previous` = `Car 3`.
4.  **Slide `Current` hand:** Move `Current` to where `Next` was pointing. So, `Current` = `Car 4`.

* **After Round 3:**
    * `Previous` = `Car 3`
    * `Current` = `Car 4`
    * `Next` = (still `Car 4` from previous step)
    * Train looks like: `null` ⬅️ `1` ⬅️ `2` ⬅️ `3`   `4` ➡️ `End` (still connected to nothing, effectively end)

**Round 4 (Working on `Car 4`):**

1.  **`Next` Hand looks ahead:** The `Next` car after `Current` (Car 4) is `End of Train` (`null`). So, `Next` = `null`.
2.  **Flip `Current`'s connection:** Make `Current` (Car 4) point *backward* to what `Previous` was pointing to (`Car 3`).
    * Now: `Car 3` ⬅️ `Car 4`
3.  **Slide `Previous` hand:** Move `Previous` to where `Current` just was. So, `Previous` = `Car 4`.
4.  **Slide `Current` hand:** Move `Current` to where `Next` was pointing. So, `Current` = `null`.

* **After Round 4:**
    * `Previous` = `Car 4`
    * `Current` = `null` (We've reached the end!)
    * Train looks like: `null` ⬅️ `1` ⬅️ `2` ⬅️ `3` ⬅️ `4`

**You're Done!**

When `Current` becomes `null`, it means you've visited and re-hooked every car. The `Previous` hand is now pointing to the *new beginning* of your reversed train (`Car 4`)!

So, the connections are now effectively:
`Car 4` ➡️ `Car 3` ➡️ `Car 2` ➡️ `Car 1` ➡️ `null` (end)

Why is this useful?

* Saves Memory: You didn't have to make a whole new copy of the train cars. You just tweaked the existing connections. This is super important in programming when you're dealing with huge amounts of data.
* Specific Algorithms: Some problems specifically need data to be reversed in this way for clever solutions.

---
Breadth-First Search (BFS)
Hey there! Imagine you're playing a video game, and you're in a giant castle with lots of rooms, hallways, and secret passages. You want to find a hidden treasure, but you want to explore the castle in a very organized way: you want to visit all the rooms on the floor you're currently on before you even think about going up or down stairs to other floors.

This is exactly what the **Breadth-First Search (BFS) Pattern** is all about! It's a way to explore things (like rooms in a castle, friends in a social network, or locations on a map) layer by layer, or level by level.

Think of it like ripples in a pond:

When you drop a stone in water, the ripples spread out in circles. BFS explores outwards from a starting point in a similar way:

1.  Your Starting Point: You start in one room (let's say the Grand Hall). This is your first "level."
2.  Level 1 Exploration: You visit all the rooms directly connected to the Grand Hall (e.g., the Kitchen, the Dining Room, the Library). These are all on "Level 1" relative to your start.
3.  Level 2 Exploration: After you've visited all of Level 1's rooms, then you go to the rooms directly connected to the Kitchen, Dining Room, and Library (but only if you haven't visited them already). These would be on "Level 2."
4.  Keep Expanding: You continue this process, visiting all rooms on the current level before moving to the next deeper level, until you find what you're looking for or you've visited every reachable room.

The "To-Do List" (Queue):

To keep track of which rooms to visit next, you need a special "to-do list." In programming, this is called a **Queue**. Think of a queue like a line at a movie theater: the first person to get in line is the first person to get their ticket.

Here's how you'd explore the castle using BFS steps:

1.  Step 1: Start and Initial To-Do:
    * Put the Grand Hall on your "to-do list" (your Queue).
    * Mark the Grand Hall as "visited" so you don't go back to it.

2.  Step 2: Get the Next Room:
    * Take the very first room off your "to-do list" (which is Grand Hall).

3.  Step 3: Explore Neighbors:
    * Look at all the rooms directly connected to the Grand Hall (e.g., Kitchen, Dining Room, Library).

4.  Step 4: Add New Rooms to To-Do:
    * For each of those connected rooms:
        * If you haven't visited it yet:
            * Add it to the end of your "to-do list."
            * Mark it as "visited."

    * Your "to-do list" might now look like: [Kitchen, Dining Room, Library]

5.  Step 5: Repeat!
    * Go back to Step 2. Take Kitchen off the list. Explore rooms connected to Kitchen. Add any new, unvisited rooms to the end of the list.
    * Then take Dining Room off, explore its neighbors, etc.
    * You keep doing this until your "to-do list" is completely empty, meaning you've explored everything reachable.

Why is this pattern super useful?

* Shortest Path: BFS is awesome for finding the *shortest path* between two points (like the fewest number of rooms to get to the treasure). Because it explores level by level, the first time you reach your destination, you know it's the shortest path.
* Social Networks: Finding friends of friends (your friends are Level 1, their friends are Level 2, etc.).
* Game Level Design: Exploring all reachable areas in a game map.
* Web Crawlers: Like search engines exploring web pages (visiting all links on one page before going deeper).

---
Depth-First Search (DFS) Pattern

Remember how we talked about exploring a giant castle level by level, like ripples in a pond (that was BFS)? Well, the **Depth-First Search (DFS) Pattern** is another super cool way to explore that castle, but it's like an adventurous explorer who picks one path and goes as deep as possible down that path before trying another!

Think of it like this:

Imagine you're in the Grand Hall of that huge castle.

1.  Pick a Door, Go Deep! You choose one door (say, the one to the Kitchen). You go into the Kitchen.
2.  Keep Going! From the Kitchen, you immediately choose another door (maybe to the Pantry). You go into the Pantry.
3.  Deeper and Deeper! From the Pantry, you might find a secret passage to an old Cellar. You go into the Cellar.
4.  Hit a Dead End? You keep going down this path (Kitchen -> Pantry -> Cellar -> Secret Tunnel) until you hit a wall, a locked door, or a room you've already seen. You can't go any deeper on this path.
5.  Backtrack! Only when you hit a dead end do you turn around and go back just enough to find the last spot where you had another choice. Maybe you go back to the Pantry, and now you see another door you didn't take before. You try that door and go deep down that new path!
6.  Repeat: You keep exploring this way – go deep, hit a dead end, backtrack, try another path – until you've explored everywhere.

The "Memory Pile" (Stack):

To remember where you need to backtrack to, you use a special "memory pile." In programming, this is called a **Stack**. Think of a stack like a pile of plates: you put new plates on top, and you always take the top plate off when you need one. So, the last thing you put on is the first thing you take off (Last-In, First-Out).

Here's how you'd explore the castle using DFS steps:

1.  Step 1: Start and Initial Memory:
    * Put the Grand Hall on your "memory pile" (your Stack).
    * Mark the Grand Hall as "visited."

2.  Step 2: Get a Room to Explore:
    * Take the very top room off your "memory pile" (which is Grand Hall).

3.  Step 3: Choose a Neighbor to Go Deep On:
    * Look at the rooms connected to the Grand Hall (e.g., Kitchen, Dining Room, Library).
    * Pick one of these that you haven't visited yet (let's say Kitchen).

4.  Step 4: Add to Memory and Dive Deep!
    * Add Kitchen to the top of your "memory pile."
    * Mark Kitchen as "visited."
    * Crucially: Now, you immediately go to Step 2 and work on Kitchen, taking it right off the top of the pile to explore its neighbors.

    * Your "memory pile" might now look like: [Library, Dining Room, Kitchen] (if you pushed them in that order, with Kitchen on top).

5.  Step 5: Keep Going, Backtracking When Needed:
    * You'll keep repeating this. If you take Kitchen off, find Pantry, put Pantry on, and immediately explore Pantry.
    * If Pantry has no unvisited neighbors (it's a dead end), then when you take Pantry off, you'll find Dining Room (or whatever was next on the stack) and start exploring *its* path.

Why is this pattern super useful?

* Finding Any Path: If you just need to know if there's a way from room A to room B (not necessarily the shortest), DFS works great.
* Maze Solving: It's like a person trying to solve a maze by always going forward until they hit a wall, then backtracking.
* Checking Connectivity: Seeing if all parts of a network are connected to each other.
* Topological Sort: A fancy way of ordering tasks that depend on each other (like building steps).
* Detecting Cycles: Finding if there's a loop in your connections (like our "loopy train" from before!).

---
Two Heaps Pattern
Imagine you're playing a game where numbers keep popping up one by one, and your job is to always know what the middle number is among all the numbers you've seen so far. This "middle number" is called the median.

If you just had a list, finding the median would mean sorting the whole list every time a new number arrives, which can be slow if you have tons of numbers!

This is where the **Two Heaps Pattern** comes in – it's a super clever way to keep track of the median efficiently using two special "boxes" or "piles" of numbers.

Meet Your Two Special Boxes (Heaps):

Think of a "heap" as a magical, self-organizing pile of numbers.

1.  The "Small Numbers" Box (Max-Heap):
    * This box will hold all the numbers that are smaller than the median.
    * Its magic trick: The **biggest number** *inside* this box always floats to the very top, like a lid. So, you always know the largest of the "small numbers." We call this a **Max-Heap** because the max number is always at the top.

2.  The "Big Numbers" Box (Min-Heap):
    * This box will hold all the numbers that are larger than the median.
    * Its magic trick: The **smallest number** *inside* this box always floats to the very top, like a lid. So, you always know the smallest of the "big numbers." We call this a **Min-Heap** because the min number is always at the top.

The Goal:

The goal is to keep these two boxes balanced, so that:
* The "Small Numbers" box contains roughly half the numbers (the smaller half).
* The "Big Numbers" box contains roughly the other half (the larger half).
* The **median** will always be either the number on top of the "Small Numbers" box, or the number on top of the "Big Numbers" box, or sometimes an average of the two!

How the Magic Works (Step-by-Step):

Let's say numbers start arriving: 5, 2, 8, 1, 9, 4

* Initial:
    * Small Numbers Box (Max-Heap): []
    * Big Numbers Box (Min-Heap): []

1.  New Number: `5`
    * Put `5` into the "Small Numbers" box (because it's the first number, it has nowhere else to go).
    * Small Numbers Box: [5] (Top: 5)
    * Big Numbers Box: []
    * **Median:** 5 (Only one number, it's the middle)

2.  New Number: `2`
    * `2` is smaller than the top of the "Small Numbers" box (`5`). So, put `2` into the "Small Numbers" box.
    * Small Numbers Box: [5, 2] (Heap organizes it so 5 is still on top)
    * **Balance Check:** The "Small Numbers" box has 2 items, "Big Numbers" box has 0. This is unbalanced!
    * Move the top from "Small Numbers" box (5) to "Big Numbers" box.
    * Small Numbers Box: [2] (Top: 2)
    * Big Numbers Box: [5] (Top: 5)
    * **Median:** Now, both boxes have 1 item. The median is the average of their tops: (2 + 5) / 2 = 3.5

3.  New Number: `8`
    * `8` is larger than the top of the "Small Numbers" box (`2`). So, put `8` into the "Big Numbers" box.
    * Small Numbers Box: [2] (Top: 2)
    * Big Numbers Box: [5, 8] (Heap organizes it so 5 is still on top)
    * **Balance Check:** Balanced (1 item in Small, 2 in Big).
    * **Median:** Now, "Big Numbers" box has one more item. The median is the top of the "Small Numbers" box (which is the smaller half): 2 (No, wait, this is wrong. If Big is larger, we take from there, or correct logic to ensure small is always slightly larger or equal). Let's fix this rule: The "Small Numbers" box will either have the same number of items as the "Big Numbers" box, or one more item.

    *Let's re-do the balance check from step 3 with the correct rule:*
    * Small Numbers Box: [2] (1 item)
    * Big Numbers Box: [5, 8] (2 items)
    * "Big Numbers" box is bigger. We need "Small Numbers" to be equal or one larger.
    * Move the top from "Big Numbers" box (5) to "Small Numbers" box.
    * Small Numbers Box: [2, 5] (Heap organizes so 5 is on top)
    * Big Numbers Box: [8] (Top: 8)
    * **Median:** Now both boxes have 2 items. Median is average of tops: (5 + 8) / 2 = 6.5

4.  New Number: `1`
    * `1` is smaller than the top of the "Small Numbers" box (`5`). So, put `1` into the "Small Numbers" box.
    * Small Numbers Box: [5, 2, 1] (Heap organizes so 5 is on top)
    * Big Numbers Box: [8] (Top: 8)
    * **Balance Check:** "Small Numbers" box has 3 items, "Big Numbers" box has 1. "Small Numbers" is too big (more than 1 extra).
    * Move the top from "Small Numbers" box (5) to "Big Numbers" box.
    * Small Numbers Box: [2, 1] (Heap organizes so 2 is on top)
    * Big Numbers Box: [8, 5] (Heap organizes so 5 is on top)
    * **Median:** Both boxes have 2 items. Median is average of tops: (2 + 5) / 2 = 3.5

This pattern keeps working for any new numbers that come in!

Why is this pattern super useful?

* Finding the Median (or Kth smallest/largest): It's the go-to method for finding the median efficiently in a continuous stream of data without sorting everything repeatedly.
* Resource Management: Imagine you have a bunch of tasks with different priorities, and you always need to know the middle-priority task.
* Any time you need to maintain two sorted halves of data.

---
Subset
Imagine you're at an ice cream shop, and they have a special deal: you can choose any combination of toppings you want!

Let's say they have just a few toppings available:
* Sprinkles (S)
* Chocolate Chips (C)
* Gummy Bears (G)

A "**Subset**" is just any group of these toppings you can pick. It could be:
* No toppings at all (just plain ice cream!)
* Just Sprinkles
* Just Chocolate Chips
* Sprinkles AND Chocolate Chips
* All three: Sprinkles, Chocolate Chips, AND Gummy Bears!

The **Subset Pattern** in programming is a cool way to systematically figure out *all* possible combinations (subsets) you can make from a given list of items.

The "Building Block" Strategy:

Imagine you're building up your topping combinations one ingredient at a time.

1.  Start with Nothing (The Empty Bowl):
    * Initially, you have only one possible combination: an empty bowl (no toppings).
    * [] (This means an empty set of toppings)

2.  Consider the First Topping (Sprinkles - S):
    * Now, look at "Sprinkles." For *every* combination you already have (which is just [] right now), you have two choices:
        * **Choice 1: Don't add Sprinkles.** Your combination stays the same: []
        * **Choice 2: Add Sprinkles.** Your combination becomes: [S]
    * So, after considering Sprinkles, your possible combinations are: [], [S]

3.  Consider the Second Topping (Chocolate Chips - C):
    * Now, take *each* of your current combinations ([] and [S]) and do the same thing for "Chocolate Chips":
        * **For []:**
            * Don't add C: []
            * Add C: [C]
        * **For [S]:**
            * Don't add C: [S]
            * Add C: [S, C]
    * So, after considering Chocolate Chips, your possible combinations are: [], [S], [C], [S, C]

4.  Consider the Third Topping (Gummy Bears - G):
    * Again, take *each* of your current combinations ([], [S], [C], [S, C]) and do the same thing for "Gummy Bears":
        * **For []:** [], [G]
        * **For [S]:** [S], [S, G]
        * **For [C]:** [C], [C, G]
        * **For [S, C]:** [S, C], [S, C, G]
    * So, after considering Gummy Bears, your *final* list of all possible combinations (subsets) is:
        `[], [S], [C], [S, C], [G], [S, G], [C, G], [S, C, G]`

See how we systematically built up all the options? For each new item, you essentially **double** the number of combinations you have, because every existing combination gets a "with" version and a "without" version of the new item.

Why is this pattern useful in programming?

* Generating Options: If you have a set of features and want to know all possible bundles of features.
* Finding Combinations: When you need to select a group of items from a larger list.
* Password Cracking (in a simplified way): Trying all possible combinations of characters (though real passwords are much more complex).
* Decision Making: Exploring all possible scenarios or choices.

---
Modified Binary Search
Remember how we talked about **Binary Search**? It's like finding a specific page in a super thick book. You open to the middle, see if your page number is higher or lower, and then ignore half the book. You keep doing that until you find your page! Super fast!

Well, **Modified Binary Search** is like using that same super-fast trick, but with a *little twist* in the rules. Sometimes, you don't want to find the *exact* page number. Or maybe the book itself is a bit messed up but still mostly organized.

Let's look at some "twists":

Twist 1: Finding the "First Time" Something Appears (or the "Last Time")
Imagine your book has the word "Magic" on many pages. You don't just want *any* page with "Magic"; you want the **very first page** where "Magic" appears.

* Regular Binary Search: Might find page 100 with "Magic." Great! But maybe page 98 also has "Magic."
* Modified Binary Search:
    1.  You still find the middle page.
    2.  If it has "Magic": "Aha! This *might* be the first one." You save this page number as a possible answer.
    3.  **The Twist:** To check if there's an *even earlier* "Magic" page, you don't stop! You still tell your "search helper" to look at the *left half* of the book (pages before your current one) to see if it can find an earlier "Magic" page.
    4.  If the middle page *doesn't* have "Magic" (or your target is bigger), you go to the right half.

This way, you keep narrowing down the search, always trying to go left if you find your item, to make sure you get the *earliest* one. The same logic (but going right) applies if you want the "last occurrence."

Twist 2: Finding the "Closest" Page (or the "Next Biggest" / "Next Smallest")
What if you're looking for page 15, but someone ripped out page 15? You want to find the page that's just *after* it, say page 16 (the "ceiling" in math terms).

* Regular Binary Search: Would just say "page 15 not found!"
* Modified Binary Search:
    1.  You find the middle page.
    2.  If the middle page is your exact target (15): Great!
    3.  If the middle page is *too small* (e.g., page 10 for target 15): You know your answer must be to the right, so you move your "start" pointer to the middle + 1.
    4.  **The Twist:** If the middle page is *too big* (e.g., page 20 for target 15): This page 20 *could be* the "next biggest" page you're looking for! So, you save 20 as a possible answer. But then, you still tell your "search helper" to look at the *left half* (pages before 20) to see if there's an even *smaller* page that's *still* greater than 15 (like page 16). You move your "end" pointer to the middle - 1.

This way, you're always trying to find the best possible "next biggest" (or "next smallest") while still using the binary search speed.

Twist 3: Finding a Page in a "Rotated" Book
Imagine your sorted book was dropped, and the first few chapters broke off and landed at the end. So, it's like: [Chapter 4, Chapter 5, Chapter 6, Chapter 1, Chapter 2, Chapter 3] The numbers are still sorted *within* two parts, but the whole thing isn't perfectly sorted from start to end.

* Regular Binary Search: Would get totally confused!
* Modified Binary Search:
    1.  You still find the middle page.
    2.  **The Twist:** Instead of just checking if the middle is higher or lower than your target, you first figure out: "Is the left half of the book (from `start` to `mid`) sorted properly?" Or, "Is the right half (from `mid` to `end`) sorted properly?"
    3.  Once you know which half is properly sorted, you can decide:
        * If your target is *inside* that properly sorted half, you search there.
        * If your target is *not* in that properly sorted half, it *must* be in the other, "broken" half, so you search there.
    4.  You keep doing this until you find your page.

---
Top K Elements Pattern
Imagine you have a giant box filled with hundreds of your favorite trading cards. But you don't have enough space to show all of them. You only have a special display case that can hold exactly K cards (like, your Top 5 coolest cards).

As you go through your big box, you want to make sure that your display case always has the very best, the very coolest, K cards you've found *so far*.

This is exactly what the **Top K Elements Pattern** is all about in programming! It's a smart way to find the K biggest, smallest, most frequent, or "best" items from a super long list, *without* having to sort the entire list, which can take a lot of time if the list is huge.

The "Magic Display Case" (Our Special Box/Heap):

To make this work, we use a special kind of self-organizing box. It's similar to the "heap" we talked about with the Two Heaps pattern.

Let's say you want to find the **Top K *coolest*** cards. Your display case has a magic trick:

* It automatically arranges itself so that the **least cool card** *among the K cards currently inside* always sits right at the very front. This makes it easy to compare new cards with the "worst" card currently in your "best K" collection. This is called a **Min-Heap**.

How Your Magic Display Case Works (Step-by-Step for Top K Coolest):

Let's try to find the **Top 3 largest numbers** from a list: [10, 5, 20, 3, 15, 8]

* Our Magic Display Case (Min-Heap) can hold `K = 3` numbers.
* **Goal:** Keep the 3 largest numbers we've seen so far.

1.  Start Filling the Case (First 3 Numbers):
    * Number 10: Put it in. Case: [10]
    * Number 5: Put it in. Case: [5, 10] (It automatically arranges so 5 is at front)
    * Number 20: Put it in. Case: [5, 10, 20] (It automatically arranges so 5 is at front)
    * *Now, your case is full (3 numbers), and the smallest of these is 5.*

2.  New Number Arrives: `3`
    * Look at the new number (`3`).
    * Compare it to the number at the front of your case (`5`).
    * Is `3` *cooler/larger* than `5`? No, `3` is smaller.
    * **Decision:** Ignore `3`. It's not one of the top 3 largest.
    * Case remains: [5, 10, 20] (5 is still at front)

3.  New Number Arrives: `15`
    * Look at the new number (`15`).
    * Compare it to the number at the front of your case (`5`).
    * Is `15` *cooler/larger* than `5`? YES! `15` is larger than `5`.
    * **Decision:** Kick out `5` (the least cool in the case). Put `15` into the case.
    * Case automatically re-arranges: [10, 15, 20] (Now `10` is at front, as it's the smallest of these three).

4.  New Number Arrives: `8`
    * Look at the new number (`8`).
    * Compare it to the number at the front of your case (`10`).
    * Is `8` *cooler/larger* than `10`? No, `8` is smaller.
    * **Decision:** Ignore `8`.
    * Case remains: [10, 15, 20] (10 is still at front)

5.  Finished! You've looked at all the numbers. The numbers remaining in your Magic Display Case are the Top 3 largest: [10, 15, 20]!

Why is this pattern super useful?

* Leaderboards: Imagine a game with millions of players, and you just want the top 10 scores. You don't want to sort all millions of scores!
* Most Popular Items: Finding the top 5 most viewed videos or most purchased products.
* Finding Frequent Items: Like finding the top 10 most common words in a huge book.
* Resource Management: If you have limited resources and need to prioritize the most important tasks.

---
K-Way Merge Pattern
Hey there! Imagine you've been given a super important job at school: you have to combine homework papers from three different classes into one single, giant pile, and this giant pile *must* be perfectly sorted by student ID number from smallest to largest.

The good news is, each teacher already gave you their papers in perfectly sorted piles:
* Teacher A's papers: [ID 1, ID 5, ID 9]
* Teacher B's papers: [ID 2, ID 6, ID 10]
* Teacher C's papers: [ID 3, ID 7]

You have K (in this case, 3) sorted piles, and you want to merge them into one big sorted pile: [ID 1, ID 2, ID 3, ID 5, ID 6, ID 7, ID 9, ID 10]

This is what the **K-Way Merge Pattern** is all about! It's a clever and efficient way to combine many already-sorted lists into one big sorted list.

The Challenge:

How do you find the *very next* smallest student ID for your big combined pile without checking *every single paper* in *every single pile* each time? That would be really slow!

Your "Little Robot Helper" (The Min-Heap):

This is where the magic comes in! You get a special "Little Robot Helper." This robot's job is super specific:

* It can only hold one paper from the front of each of your `K` piles.
* Its special power: It always keeps the **smallest ID number** among all the papers it's holding right on its screen (at the very top)!
* This robot is called a **Min-Heap** in programming because it always keeps the *minimum* (smallest) value at its top.

How Your Robot Helps You Merge Papers (Step-by-Step):

Let's use our example piles:
* Pile A: [1, 5, 9]
* Pile B: [2, 6, 10]
* Pile C: [3, 7]

1.  Initial Setup:
    * Take the *first paper* from *each* pile and give it to your robot helper.
    * Robot's memory: [1 (from A), 2 (from B), 3 (from C)]
    * Robot's screen shows: `1` (from Pile A) - because it's the smallest.

2.  Get the First Paper for Your Big Pile:
    * Ask the robot: "What's the smallest paper you see?"
    * Robot says: "`1` (from Pile A)!" and gives you paper 1.
    * You add `1` to your big combined pile: [1]

3.  Replenish the Robot:
    * Since you just took paper `1` from Pile A, give the robot the *next* paper from Pile A (which is `5`).
    * Robot's memory: [5 (from A), 2 (from B), 3 (from C)]
    * Robot's screen updates to show: `2` (from Pile B) - because `2` is now the smallest among `5, 2, 3`.

4.  Repeat! (Get `2`):
    * Ask the robot: "What's the smallest now?" Robot says: "`2` (from Pile B)!" You add `2` to your pile: [1, 2]
    * Replenish: Give robot the next from Pile B (which is `6`).
    * Robot's memory: [5 (from A), 6 (from B), 3 (from C)]
    * Robot's screen updates to show: `3` (from Pile C).

5.  Repeat! (Get `3`):
    * Ask robot: "`3` (from Pile C)!" You add `3`: [1, 2, 3]
    * Replenish: Give robot the next from Pile C (which is `7`).
    * Robot's memory: [5 (from A), 6 (from B), 7 (from C)]
    * Robot's screen updates to show: `5` (from Pile A).

...And you keep going like this! You always take the smallest from the robot, and then give the robot the next paper from the pile that paper came from.

Why is this pattern super useful?

* Combining Sorted Data: If you have data split across many files or databases, and each part is sorted, this is how you efficiently combine them.
* External Sorting: When a list is too big to fit into your computer's memory, you can sort it in smaller chunks and then use K-Way Merge to combine those chunks.
* Large-Scale Data Processing: Essential for many big data algorithms.

---
Topological Sort Pattern
Imagine you have a bunch of chores or activities you need to do to get ready for school in the morning. But here's the tricky part: some things have to be done before others!

For example:
* You **must** `Wake Up` before you can do anything else.
* You **must** `Eat Breakfast` before you `Leave for School`.
* You **must** `Put on Socks` before you `Put on Shoes`.
* You **must** `Put on Shoes` before you `Leave for School`.

This is what we call a **Topological Sort Pattern** in programming! It's a way to find a valid order to do a bunch of tasks when some tasks depend on others being finished first.

The Big Idea: Finding a "To-Do List" Order

Your goal is to create *a* valid "to-do list" for your morning, where you never try to do something before its prerequisites are met.

The Special Helpers You'll Use:

1.  The "Dependency Counter" (In-Degree):
    * For every single task, you'll count how many other tasks *must* be completed before *this* task can start.
    * Example: `Put on Shoes` has a dependency count of 1 (because `Put on Socks` must be done first). `Wake Up` has a dependency count of 0.

2.  The "Ready-to-Do List" (Queue):
    * This is like your actual list of things you can do *right now* because all their dependencies are met.
    * It's a "queue," meaning first-in, first-out (like a line for a ride – the first one in line gets to go first).

How to Find the Order (Step-by-Step):

Let's use our morning tasks:

* `Wake Up`
* `Eat Breakfast` (depends on `Wake Up`)
* `Put on Socks` (depends on `Wake Up`)
* `Put on Shoes` (depends on `Put on Socks`)
* `Brush Teeth` (depends on `Wake Up`)
* `Leave for School` (depends on `Eat Breakfast`, `Put on Shoes`, `Brush Teeth`)

Step 1: Count Initial Dependencies (In-Degree):

* `Wake Up`: 0 dependencies
* `Eat Breakfast`: 1 (from `Wake Up`)
* `Put on Socks`: 1 (from `Wake Up`)
* `Put on Shoes`: 1 (from `Put on Socks`)
* `Brush Teeth`: 1 (from `Wake Up`)
* `Leave for School`: 3 (from `Eat Breakfast`, `Put on Shoes`, `Brush Teeth`)

Step 2: Fill Your "Ready-to-Do List":
* Put all tasks with 0 dependencies onto your "Ready-to-Do List."
* Ready-to-Do List: [Wake Up]

Step 3: Start Doing Tasks & Updating Dependencies:

* **Round 1:**
    * Take `Wake Up` from your Ready-to-Do List. (You've now done `Wake Up`!)
    * **Add to your final order:** [Wake Up]
    * Now, for every task that *depended on* `Wake Up` (`Eat Breakfast`, `Put on Socks`, `Brush Teeth`):
        * Reduce their dependency count by 1.
        * `Eat Breakfast`: count becomes 0. Add it to Ready-to-Do.
        * `Put on Socks`: count becomes 0. Add it to Ready-to-Do.
        * `Brush Teeth`: count becomes 0. Add it to Ready-to-Do.
    * Ready-to-Do List: [Eat Breakfast, Put on Socks, Brush Teeth] (order might vary depending on how you add them, but all are ready)

* **Round 2 (Let's say you take `Eat Breakfast` first):**
    * Take `Eat Breakfast` from Ready-to-Do. (Done!)
    * **Add to your final order:** [Wake Up, Eat Breakfast]
    * For tasks that depended on `Eat Breakfast` (`Leave for School`):
        * Reduce `Leave for School`'s count by 1 (it's now 2).
    * Ready-to-Do List: [Put on Socks, Brush Teeth]

* **Round 3 (Let's say you take `Put on Socks`):**
    * Take `Put on Socks`. (Done!)
    * **Add to your final order:** [Wake Up, Eat Breakfast, Put on Socks]
    * For tasks that depended on `Put on Socks` (`Put on Shoes`):
        * Reduce `Put on Shoes`'s count by 1 (it's now 0). Add it to Ready-to-Do.
    * Ready-to-Do List: [Brush Teeth, Put on Shoes]

...You continue this process until your Ready-to-Do List is empty.

**Final Order (one possible valid order):**
`[Wake Up, Eat Breakfast, Put on Socks, Brush Teeth, Put on Shoes, Leave for School]`

**Important Note: No Cycles!**

This pattern only works if there are no "cycles" in your dependencies. For example, if `Put on Socks` depended on `Put on Shoes`, and `Put on Shoes` depended on `Put on Socks`, you'd be stuck in an impossible loop! If your "Ready-to-Do List" becomes empty but you still have tasks with dependencies, it means there's a cycle.

Why is this pattern super useful in programming?

* Project Scheduling: Figuring out the order to build software components or complete project tasks.
* Course Prerequisites: Deciding which order to take classes (e.g., you need Algebra 1 before Algebra 2).
* Build Systems: Compiling code modules in the correct order when some modules depend on others.
* Dependency Resolution: Used by package managers (like `npm` or `pip`) to install software libraries in the right order.
"""

# 2. What you want the final MP3 audio file to be named
output_mp3_filename = "my_document_audio.mp3"

# --- PART 2: Function to do the work ---

def text_to_audio_file(text_content, audio_output_filename, chunk_size=3000):
    """
    Converts a long string of text into an MP3 audio file.
    Splits long text into chunks to avoid TTS service limits and combines them.
    """
    print(f"Starting text-to-speech conversion for: {audio_output_filename}")
    temp_audio_files = []
    
    # Split text into manageable chunks. Prioritize natural breaks like paragraphs and sentences.
    paragraphs = text_content.split('\n\n') 
    final_chunks = []
    current_chunk_sentences = []
    current_chunk_len = 0
    
    for para in paragraphs:
        split_sentences_in_para = [s.strip() for s in para.split('.') if s.strip()]
        
        for sentence in split_sentences_in_para:
            if current_chunk_len + len(sentence) + 2 <= chunk_size: # +2 for potential space and period
                current_chunk_sentences.append(sentence)
                current_chunk_len += len(sentence) + 2
            else:
                if current_chunk_sentences:
                    final_chunks.append(". ".join(current_chunk_sentences) + ".")
                current_chunk_sentences = [sentence]
                current_chunk_len = len(sentence) + 2
        
        if current_chunk_sentences:
            final_chunks.append(". ".join(current_chunk_sentences) + ".")
            current_chunk_sentences = []
            current_chunk_len = 0

    if not final_chunks and text_content.strip(): # Fallback for very short texts or no natural breaks
        final_chunks = [text_content[i:i + chunk_size] for i in range(0, len(text_content), chunk_size)]


    if not final_chunks:
        print("No text found or processed to convert to audio. Cannot generate audio.")
        return None

    for i, chunk in enumerate(final_chunks):
        if not chunk.strip(): # Skip empty chunks
            continue
        try:
            tts = gTTS(text=chunk, lang='en') # 'en' for English
            temp_file = f"temp_chunk_{i}.mp3"
            tts.save(temp_file)
            temp_audio_files.append(temp_file)
            print(f"  Generated audio for chunk {i+1}/{len(final_chunks)}")
        except Exception as e:
            print(f"ERROR: Could not generate audio for chunk {i+1}. Problem: {e}")
            print(f"  Problematic chunk text (first 100 chars): '{chunk[:100]}...'")
            print("  This might be due to a network issue, a very long word, or an unsupported character.")

    if not temp_audio_files:
        print("No audio chunks were successfully generated. Cannot create main audio file.")
        return None

    # Combine all temporary audio files into one
    combined_audio = AudioSegment.empty()
    for temp_file in temp_audio_files:
        try:
            audio_segment = AudioSegment.from_mp3(temp_file)
            combined_audio += audio_segment
            os.remove(temp_file) # Clean up the temporary MP3 file
        except Exception as e:
            print(f"ERROR: Could not combine audio file '{temp_file}'. Problem: {e}. This part might be missing from the final audio.")

    if not combined_audio.duration_seconds > 0:
        print("Combined audio is empty or too short. Audio file not created.")
        return None

    combined_audio.export(audio_output_filename, format="mp3")
    print(f"SUCCESS! Full audio file created: {audio_output_filename}")
    return audio_output_filename

# --- PART 3: Run the Program ---
if __name__ == "__main__":
    print("--- Starting Document to MP3 Conversion ---")
    print("Please ensure your 'document_text' variable is correctly set in the code!")

    # Convert text to audio
    generated_audio_file = text_to_audio_file(document_text, output_mp3_filename)

    if not generated_audio_file:
        print("Audio generation failed. No MP3 file was created.")

    print("\n--- Process Finished ---")