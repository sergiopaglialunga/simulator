# Requirements:

- The tracker needs to be able to track time in a consistent way
- The program starts by asking how long the simulation will run for
- Every month, a random number of trainees are generated wanting to be trained (50 - 100)
- Every 2 months, Sparta global opens a training centre. They open instantly and can take trainees every month
- A centre can train a max of 100 trainees and takes a random number of trainees every month. (0 - 50 trainees up to their capacity)
- If a centre is full, trainees can be moved to any other centre which is not full
- If all centres are full, the trainees go onto a waiting list. This list must be served first before new trainees are taken
- At the end of the simulation, output should show:
  - number of open centres
  - number of full centres
  - number of trainees currently training
  - number of trainees on the waiting list

## Extra requirements:
- Sparta will now check centres each month. If a centre has less than 25 trainees, it will close.  The trainees will be randomly moved to another suitable centre
- The simulation should now offer the choice of data at the end of the simulation or a running output updated each month
- Trainees will now have a course type (Java, C#, Data, DevOps or Business). A trainee will be randomly assigned a course when they are created. This will never change
- Sparta now has 3 different types of centre. When a new centre can be opened, one of the following will be randomly chosen
    - Training Hub: can train a maximum of 100 trainees but 3 can be opened at a time each month
    - Bootcamp: can train a maximum of 500 trainees but can remain open for 3 months if there are less than 25 trainees in attendance. If a Bootcamp has 3 consecutive months of low attendance, it will close. For the lifetime of the simulation, only 2 Bootcamps can ever exist
    - Tech Centre: Can train 200 trainees but only teaches one course per centre. This is chosen randomly when a Tech Centre is open
- The simulation should report on the following:
    - number of open centres (breakdown for each type)
    - number of closed centres (breakdown for each type)
    - number of full centres (breakdown for each type)
    - number of trainees currently training (breakdown for each type)
    - number of trainees on the waiting list (breakdown for each type)
-	Number of clients
-	Number of trainees on client assignment

The trainee can be moved to another centre teaching the same course

## Last requirements
- If a trainee has been in training for a year, they are moved to a bench state
- Clients will begin to be randomly created after 1 year of the simulation (one each year)
- A client will have a requirement when they are created e.g a need for 27 Java trainees.  The requirement can be any value greater than or equal to 15 to 30
- A client will take a random number of trainees from the bench each month (1 - full requirement) until their requirement is met
- A client will only take one type of trainee (Java, C#, Data, DevOps or Business)
- If a client does not collect enough trainees from the bench within a year, they will leave unhappy
- The trainees not taken will go back to the bench
- If a client does collect enough trainees from the bench within a year, they will leave happy and return the next year with the same requirement



