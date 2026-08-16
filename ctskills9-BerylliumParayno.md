# Computational Thinking Exercise: “Smart School Canteen Queue”

# Section:** 9 - Beryllium  
# / Name:** Dexter Josue A. Parayno  
# **Date:** 08/15/2026  
# **Score:** ___________

### Scenario


The PSHS school canteen is small and often gets crowded during lunch break.

Students line up to buy food, but the process is slow because:

- Some students take too long to decide what to order.
- The cashier has to manually calculate totals and give change.
- There is no system to track which food items are running out.

Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

## Step 1: Identify the Big Problem

**Main Problem:** The PSHS school canteen doesn’t have enough space for a lot of people, so it often gets packed up during lunch break. When students line up to buy food, the process often takes so long because some do not know what to order, and the cashier has to calculate everything manually. Moreover, tracking food items that are running out is inexecutable.

## Step 2: Identify three to four Sub-Problems

Please list possible sub-problems:

1. The ordering process lacks organization, which results in long lines, taking so much time for the buyers to finish ordering.

2. Students do not know what to order, slowing down the process.

3. The cashier has to manually calculate the total cost of the student’s purchases, and give change, lacking efficiency.

4. There is no system for tracking depleting food items, therefore the buyers and the cashier won’t know what items are available and unavailable.

## Step 3: Define Computational Thinking Approaches

For each sub-problem, apply CT skills:

# 1. The ordering process lacks organization.

**CT Skill:** Decomposition

**Example Solution:**

Decompose the process into easier steps:

1. Choose what to buy.
2. Place order.
3. Calculate total.
4. Receive food.
5. Inventory update.

# 2. Students do not know what to order.

**CT Skill:** Abstraction

**Example Solution:**

Design a simple and direct digital menu displaying food options, prices, and items available, so students can make choices prior to approaching the cashier.

# 3. The cashier has to manually calculate the total cost of the student’s purchases, and give change.

**CT Skill:** Algorithm Design

**Example Solution:**

Create a program that adds the prices of selected items, compares the total with the amount paid, and automatically calculates the change.

# 4. There is no system for tracking depleting food items.

**CT Skill:** Pattern Recognition

**Example Solution:**

Analyze and record how many units of each food are sold and identify the pattern in which items are often purchased so the canteen can prepare enough stock for the next few days.

## Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem


START

Display the available food items and its prices.

Student chooses what food item/s to buy.

Check if food items are available

IF an item is unavailable:

    Display “Item is unavailable, choose another one.”

    The student selects another one

ENDIF

Calculate total price of purchase

Display the total price

Ask student for payment

IF payment is less than total price

    Display "Insufficient payment"

    Ask for payment again

ELSE

    Calculate change

    Display change

    Give order to student
    
ENDIF

## REFLECTION:
For me, decomposing the canteen problem makes it easier to understand because the main problem can be divided into smaller tasks such as ordering, payment, inventory, and queue management. Each task can then be addressed using computational thinking skills. These computational thinking skills are as such: decomposition breaks the process into manageable parts, abstraction focuses on the important information needed by the system, pattern recognition helps identify commonly purchased foods, and algorithm design creates clear steps, which I did in the form of pseudocode, that a computer can follow. This approach could help make the canteen faster and more organized while reducing calculation errors and waiting time.
