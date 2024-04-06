<h1 style="text-align: center;">Mathematics Trainer</h1>

## Foreword

Once upon a time, my children were studying in elementary school.
I have two of them, and since I, as the father and a mathematician
in our family, they all used to come to me together with all the math
homework. The main task almost every day was to solve 10 to 20 examples
of elementary operations: addition, subtraction, multiplication
and division. Everything was very simple, but the most important thing was
to come up with them first, and that task is not for the faint-hearted.
After a month of brainstorming, I broke down and completed this little project
at once, and learned Python in the process.

## Description

Run task_create.py and enter some data to specify the conditions. After
the script finishes running, you will see a table of 4 columns by 12 rows
with examples on the screen.

## Exemple

run script by command:
```shell
python task_create.py
```
you can see:
```
Note:
 The value in (<val>) will be the default value.
Enter learner name: 1-Timur or 2-Arina or (Guest) or name? 
```
Enter: 1, 2, 'NameOfPerson', (skip or leave blank)=Guest   
```
Choose quality of test (1-simple) or 2-complex?
```
Enter: 1 or 2, (skip or leave blank)=1
```
Enter variants for first element (1-12)?
Enter variants for second element (1-12)?
```
Enter: The numbers you need, separating them by commas.
```
Enter list operation (sum, sub, div, mul)? 
```
Enter: The operations you need, separating them by commas.
```
Do change title? (y/N):
```
If you enter 'y' or 'Y', the header of the table will be 'Trace d'etude';
otherwise, it will be 'Test for'.
```
        Trace d'etude date yyyy-mm-dd Guest (simple)
        +----------------+----------------+----------------+----------------+
        |  7  + 12  =    | 16  -  4  =    | 63  ÷  7  =    | 12  × 10  =    |
        +----------------+----------------+----------------+----------------+
        | 11  + 12  =    | 22  - 12  =    |  8  ÷  4  =    |  7  ×  5  =    |
        +----------------+----------------+----------------+----------------+
        |  9  +  3  =    | 23  - 11  =    | 12  ÷  3  =    |  4  ×  8  =    |
        +----------------+----------------+----------------+----------------+
        |  7  + 10  =    |  7  -  3  =    | 21  ÷  7  =    | 12  ×  8  =    |
        +----------------+----------------+----------------+----------------+
        |  6  +  9  =    | 15  - 11  =    | 54  ÷  9  =    |  8  ×  2  =    |
        +----------------+----------------+----------------+----------------+
        | 11  +  7  =    | 15  -  3  =    | 44  ÷  4  =    | 10  ×  4  =    |
        +----------------+----------------+----------------+----------------+
        | 12  +  6  =    | 14  - 12  =    | 30  ÷  5  =    |  3  × 11  =    |
        +----------------+----------------+----------------+----------------+
        |  2  + 12  =    | 16  -  6  =    | 24  ÷  8  =    |  2  × 12  =    |
        +----------------+----------------+----------------+----------------+
        |  4  +  2  =    | 14  -  3  =    | 24  ÷  3  =    | 11  ×  9  =    |
        +----------------+----------------+----------------+----------------+
        |  6  + 10  =    |  8  -  6  =    | 72  ÷  8  =    |  5  ×  9  =    |
        +----------------+----------------+----------------+----------------+
        | 10  + 11  =    | 20  -  8  =    | 77  ÷  7  =    |  5  ×  2  =    |
        +----------------+----------------+----------------+----------------+
        |  5  +  4  =    | 17  -  8  =    | 96  ÷ 12  =    | 10  ×  8  =    |
        +----------------+----------------+----------------+----------------+
        Trace d'etude date 2024-04-05 Guest (simple)
        +----------------+----------------+----------------+----------------+
        |  7  + 12  =19  | 16  -  4  =12  | 63  ÷  7  = 9  | 12  × 10  =120 |
        +----------------+----------------+----------------+----------------+
        | 11  + 12  =23  | 22  - 12  =10  |  8  ÷  4  = 2  |  7  ×  5  =35  |
        +----------------+----------------+----------------+----------------+
        |  9  +  3  =12  | 23  - 11  =12  | 12  ÷  3  = 4  |  4  ×  8  =32  |
        +----------------+----------------+----------------+----------------+
        |  7  + 10  =17  |  7  -  3  = 4  | 21  ÷  7  = 3  | 12  ×  8  =96  |
        +----------------+----------------+----------------+----------------+
        |  6  +  9  =15  | 15  - 11  = 4  | 54  ÷  9  = 6  |  8  ×  2  =16  |
        +----------------+----------------+----------------+----------------+
        | 11  +  7  =18  | 15  -  3  =12  | 44  ÷  4  =11  | 10  ×  4  =40  |
        +----------------+----------------+----------------+----------------+
        | 12  +  6  =18  | 14  - 12  = 2  | 30  ÷  5  = 6  |  3  × 11  =33  |
        +----------------+----------------+----------------+----------------+
        |  2  + 12  =14  | 16  -  6  =10  | 24  ÷  8  = 3  |  2  × 12  =24  |
        +----------------+----------------+----------------+----------------+
        |  4  +  2  = 6  | 14  -  3  =11  | 24  ÷  3  = 8  | 11  ×  9  =99  |
        +----------------+----------------+----------------+----------------+
        |  6  + 10  =16  |  8  -  6  = 2  | 72  ÷  8  = 9  |  5  ×  9  =45  |
        +----------------+----------------+----------------+----------------+
        | 10  + 11  =21  | 20  -  8  =12  | 77  ÷  7  =11  |  5  ×  2  =10  |
        +----------------+----------------+----------------+----------------+
        |  5  +  4  = 9  | 17  -  8  = 9  | 96  ÷ 12  = 8  | 10  ×  8  =80  |
        +----------------+----------------+----------------+----------------+
```
Also, the script creates a text file named ```task_to_print``` which you can print out.