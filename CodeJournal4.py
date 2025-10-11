class cat:
    def __init__(self, arm_length_m, leg_length_m, eye_count, has_tail, is_furry):
        self.arm_length = arm_length_m 
        self.leg_length = leg_length_m 
        self.number_of_eyes = eye_count   
        self.has_a_tail = has_tail   
        self.is_furry = is_furry

    def describe(self): 
        print("--- Animal Characteristics ---")
        print(f"The animal's arm length is: {self.arm_length:.2f} meters")
        print(f"The animal's leg length is: {self.leg_length:.2f} meters")
        print(f"It has {self.number_of_eyes} eyes.")
        print(f"Does it have a tail? {'Yes' if self.has_a_tail else 'No'}")
        print(f"Is it furry? {'Yes' if self.is_furry else 'No'}")
        print("------------------------------")

if __name__ == "__main__":
    my_favorite_animal = cat(
        arm_length_m=0.23,
        leg_length_m=0.23,
        eye_count=2,
        has_tail=True,
        is_furry=True
    )

    # 2. Call the member function to print the description
    my_favorite_animal.describe()