class Employee{
    //instance variable
    int cardid;

    //constructor
    public Employee(int cardid){
        this.cardid=cardid;
    }

    //method

    public String getPunchInTime(int startTime, int endTime){
        int diff = endTime-startTime;
        return this.cardid+" User spent time as :"+diff;
    }

    
}
    //instance of class
    
    Employee e1 = new Employee(45);
    e1.cardid;
    e1.getPunchInTime(44,88);
