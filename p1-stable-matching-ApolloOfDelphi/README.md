[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=13445637&assignment_repo_type=AssignmentRepo)

Assignment is due at 11:59pm on February 1st, 2024. You may submit a lateness coupon request BEFORE the assignment is due by sending an email to weiping-pei@utulsa.edu with Subject "CYB 2013 Project Lateness Coupon". All other late work will receive a 10 percentage point deduction per day (including weekends), No late work is accepted beyond five days after the assignment is due.

The Gale-Shapley algorithm can be modified to accommodate many variations on the Stable Matching Problem. Your task is to implement the following two variations in Python. The code is turned in through Github Classroom. 

 You can get feedback on whether your answers are correct through GitHub Classroom. You may make as many modifications as you would like until the code is working correctly. Please write your name(s) as a comment in the first line of code in gs.py.

Note: you are permitted to reuse code from the gs method as appropriate.

## Task A: Forbidden Matches
 
 In this variant of the Stable Matching Problem, in addition to the set of men M and women M , there is a set F ⊆ M × W of forbidden pairs that are not allowed to be matched together. Using the revised definition of stable matching on p. 20 of Algorithm Design, implement `gs_block(men,women,pref,blocked)`, where `blocked` is a set of forbidden pairs, for example, of the form:
`blocked = {('xavier','clare'),('zeus','clare'),('zeus','amy')}`

## Task B: Coping with indifference

In this variant of the Stable Matching Problem, ties are allowed in the preference ordering. They are implemented by turning the preference list into a list of sets, where ties are placed into the same set. Implement `gs_tie(men,women,preftie)`, where `preftie` is a dictionary mapping people to a list of sets, for example, of the form:

```python 
thepreftie = {'xavier': [{'bertha'},{'amy'},{'clare'}], 'yancey': [{'amy','bertha'},{'clare'}],
'zeus': [{'amy'},{'bertha','clare'}],
'amy': [{'zeus','xavier','yancey'}],
'bertha': [{'zeus'},{'xavier'},{'yancey'},], 'clare': [{'xavier','yancey'},{'zeus'}]
}
```
Here, Xavier strictly prefers Bertha to Amy to Clare, Yancey is indifferent between Amy and Bertha, but prefers both to Clare, and so on.
