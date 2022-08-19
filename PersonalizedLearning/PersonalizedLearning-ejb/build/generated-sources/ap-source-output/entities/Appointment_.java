package entities;

import entities.Appointmentmessage;
import entities.Student;
import java.util.Date;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:14")
@StaticMetamodel(Appointment.class)
public class Appointment_ { 

    public static volatile SingularAttribute<Appointment, Student> studentid;
    public static volatile SingularAttribute<Appointment, Date> endtime;
    public static volatile SingularAttribute<Appointment, Integer> id;
    public static volatile SingularAttribute<Appointment, Date> starttime;
    public static volatile SingularAttribute<Appointment, Appointmentmessage> appointmentmessage;

}