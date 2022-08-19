package entities;

import entities.Scheduleclass;
import entities.TeacherAdmin;
import java.util.Date;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:13")
@StaticMetamodel(Teacherschedule.class)
public class Teacherschedule_ { 

    public static volatile SingularAttribute<Teacherschedule, Scheduleclass> belongclassid;
    public static volatile SingularAttribute<Teacherschedule, Boolean> myresult;
    public static volatile SingularAttribute<Teacherschedule, Date> endtime;
    public static volatile SingularAttribute<Teacherschedule, String> memo;
    public static volatile SingularAttribute<Teacherschedule, Integer> id;
    public static volatile SingularAttribute<Teacherschedule, Date> starttime;
    public static volatile SingularAttribute<Teacherschedule, TeacherAdmin> userid;

}