package entities;

import entities.Scheduleclass;
import entities.Student;
import java.util.Date;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:14")
@StaticMetamodel(Studentschedule.class)
public class Studentschedule_ { 

    public static volatile SingularAttribute<Studentschedule, Scheduleclass> belongclassid;
    public static volatile SingularAttribute<Studentschedule, Boolean> myresult;
    public static volatile SingularAttribute<Studentschedule, String> memo;
    public static volatile SingularAttribute<Studentschedule, Date> endtime;
    public static volatile SingularAttribute<Studentschedule, Integer> id;
    public static volatile SingularAttribute<Studentschedule, Date> starttime;
    public static volatile SingularAttribute<Studentschedule, Student> userid;

}