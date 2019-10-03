**Plan for Iteration 2 - Development**

When implementing the tests for the required functions, our team discovered 
there existed inherent dependencies, where some functions would need to call
others. For instance, tokens generated from the "auth_login" function were
regularly used in the input for functions that interacted with channels and 
messages. 

With this insight, for iteration 2 we plan to implement the functions that 
interact with the *registration* and *login* of the user first. Following that the 
intention is to then implement the *user_profile* based functions which depend on
the output of the initial functions. Next we plan to complete the *channel* and
*message* based functions in the respective order. Finally we will finish the 
remaining functions which will most likely be ones that are based on 
transfering *permission* and *searching*.

Our general planned structure is a bottom up methodology, such that we can test 
the base level functions before moving up to test functions that call upon 
lower levels. In each of these stages we will have regular meetings to ensure 
functions are 100% operational and producing the expected output, before
moving up to higher level functions. This will ensure there is no ambiguity in 
which function might have problems assosciated with it when debugging. 

Overall, we anticipate the development stage will take around two weeks. During 
this time we will:

1. Indivdually complete assgined base-level functions
2. Conduct tests indivdually with the established testing functions from iter1
3. Have a group meeting to discuss any issues/challenges and rectify them.
4. Peer reveiew the code and conduct a second phase of testing.
5. Move up to higher level functions and repeat steps 1 to 4

Ofcourse it is important to consider that this is just a plan and we will 
receive more information when iteration 2 is released, our weekly meetings wil 
ensure that the team receptive to the new requirements and account for them in 
our development approach.