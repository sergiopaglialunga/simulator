import random
from random import randrange

trainees = []
clients = []
centres = []

# condition = training, waiting_list, client, bench
class Trainee:
    def __init__(self, course, condition):
        self.course = course
        self.condition = condition
        # every month this value will increase when the trainee is in condition == "training"

        self.month = 0

# condition = open, full, closed
class Centre:
    def __init__(self):
        pass

    def distribute_trainees(self):
        # 9) check if the centre is still open before assigning trainees
        if centre.condition == "open":
            rand = random.randint(0, 50)
            # check for number of vacancies in the center
            vacancies = centre.capacity - centre.trainees
            if vacancies < rand:
                # the center will only take the number of trainees = to the vacancies
                rand = vacancies

            while rand >= 0:
                # assign trainees to learning centres
                for trainee in trainees:
                    if trainee.condition == "waiting_list":
                        # NEXT: what happens if the center is a Tech Center that only teaches 1 course ??????????!!!!!
                        if centre.kind == "Tech Center" and centre.course.key() == trainee.course:
                            trainee.condition = "training"
                            centre.course[trainee.course].append(trainee)
                        else:
                            trainee.condition = "training"
                            centre.course[trainee.course].append(trainee)
                        # 10) check if the centre is full after assigning trainees
                        if centre.trainees == centre.capacity:
                            centre.condition = "full"
                        rand -= 1
                        if rand == 0:
                            break
                break

    def check_trainees(self):
        # 12) close bootcamps with less than 25 trainees for 3 months
        if centre.kind == "Bootcamp" and centre.trainees < 25:
            centre.close_BC += 1
            if centre.close_TH == 4:
                centre.condition = "closed"
                # 14) move trainees to other centres
                centre.move_trainees()
        if centre.kind == "Bootcamp" and centre.trainees >= 25:
            centre.close_BC = 0
        # 13) close centres with less than 25 trainees
        if (centre.kind == "Training Hub" or centre.kind == "Tech Centre") and centre.trainees < 25:
                centre.condition = "closed"
                # move trainees to waiting list
                centre.move_trainees()

    def move_trainees(self):
        # 14) move trainees to waiting list
        # iterate over the dictionary - trainee is a list containing the trainees studying in each course
        for trainee in centre.course.values():
            # iterate over the items in the list containing the trainees studying in each course
            # t is each of the trainees
            for t in len(trainee):
                t.condition = "waiting_list"
                # remove the trainee (t) from the list trainee
                trainee.remove(t)

# can train a maximum of 100 trainees but 3 can be opened at a time each month
class TrainingHub(Centre):
    def __init__(self, condition, month):
        self.course = {"Java": [], "C#": [], "Data": [], "DevOps": [], "Business": []}
        self.condition = condition
        self.month = month
        self.kind = "Training Hub"
        self.capacity = 100
        self.trainees = 0
        self.close_TH = 0

        # MOVE TO A METHOD
        n_trainees = 0
        for t_list in self.trainees.values():
            n_trainees += len(t_list)
        if n_trainees >= 100:
            self.condition = "full"

# can train a maximum of 500 trainees
class Bootcamp(Centre):
    def __init__(self, condition, month):
        self.course = {"Java": [], "C#": [], "Data": [], "DevOps": [], "Business": []}
        self.condition = condition
        self.month = month
        self.kind = "Bootcamp"
        self.trainees = 0
        self.capacity = 500

        n_trainees = 0
        for t_list in self.trainees.values():
            n_trainees += len(t_list)
        if n_trainees >= 500:
            self.condition = "full"

# Can train 200 trainees but only teaches one course per centre
# when I open this kind of centre I will randomly assign a kind of course
class TechCentre(Centre):
    def __init__(self, condition, month):
        self.course = {}
        self.condition = condition
        self.month = month
        self.kind = "Tech Centre"
        self.trainees = 0
        self.capacity = 100

        n_trainees = 0
        for t_list in self.trainees.values():
            n_trainees += len(t_list)
        if n_trainees >= 500:
            self.condition = "full"


class Clients:
    def __init__(self, trainee_req, course, month):
        self.trainee_req = trainee_req
        self.trainees_taken = []
        self.course = course
        self.month = month

    def assign_trainees(self):
            # check if the client needs trainees
            if len(client.trainees_taken) < client.trainee_req:
                # calculate the number of trainees needed
                trainees_needed = client.trainee_req - len(client.trainees_taken)
                # assign trainees to existing clients
                while trainees_needed > 0:
                    for trainee in trainees:
                        if trainee.condition == "bench":
                            if trainee.course == client.course:
                                client.trainees_taken.append(trainee)
                                trainees_needed -= 1

        def move_trainees(self):
            for trainee in client.trainees_taken:
                trainee.condition = "bench"

        def unsatisfied_client(self):
            if len(client.trainees_taken) < client.trainee_req and num - client.month == 12:
                # move trainees to bench and delete client
                for trainee in client.trainees_taken:
                    trainee.condition = "bench"
                    clients.remove(client)

user_months = int(input(" Enter the number of months for the simulation:\n"))
user_option = int(input(" For monthly results enter: 1\n For results at the end enter: 2 \n"))

num = 1
while num <= user_months:
    # Every 2 months
    if num % 2 == 0:
        # 15) open 1 centre
        # check if less than 2 bootcamps are open
        center_type = random.choice("Training Hub", "Bootcamp", "Tech Centre")
        if center_type == "Bootcamp":
            count = 0
            for i in range(0,len(centres)-1):
                if centres[i].type == "Bootcamp" and centres[i].condition == "open":
                    count += 1
            if count < 2:
                centres.append(Bootcamp("open", num))
            # else choose between Training Hub or Tech Centre


        elif center_type == "Training Hub":
            count = 0
            for i in range(0,len(centres)-1):
                if centres[i].type == "Training Hub" and centres[i].condition == "open":
                    count += 1
            if count < 3:
                centres.append(TrainingHub("open", num))



    # 1) increase the month value for the trainees doing training
    for trainee in trainees:
        if trainee.condition == "training":
            trainee.month += 1
        # 2) after 12 months of training move trainees to bench
        if trainee.month == 12:
            trainee.condition = "bench"
    # 3) assign trainees to existing clients
    for client in clients:
        # check if the client needs trainees
        client.assign_trainees()
        # 4) move trainees with unsatisfied client to bench before deleting the client
        client.move_trainees()
        # 5) delete unsatisfied clients (didn't fulfill requirement within a year)
        client.unsatisfied_client()

    # 6) create 50 to 100 new trainees
    num_trainees = random.randrange(50, 100)
    while num_trainees > 0:
        # 7) random assignment of trainee to courses
        option = random.choice(["Java", "C#", "Data", "DevOps", "Business"])
        # create a new trainee and append it to the trainees dictionary
        trainees.append(Trainee(option, "waiting_list", num))

    # 8) each center takes 0 to 50 trainees
    for centre in centres:
        # trainees taken by centres
        centre.distribute_trainees()
        # 11) check for number of trainees for centre
        # 12) close bootcamps with less than 25 trainees for 3 months
        # 13) close centres with less than 25 trainees
        centre.check_trainees()
        # 14) move trainees to another centre
        centre.move_trainees()




    num += 1

print(Trainee)
