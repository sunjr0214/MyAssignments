package entities;

import entities.Appointment;
import entities.TeacherAdmin;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:14")
@StaticMetamodel(Appointmentmessage.class)
public class Appointmentmessage_ { 

    public static volatile SetAttribute<Appointmentmessage, Appointment> appointmentSet;
    public static volatile SingularAttribute<Appointmentmessage, TeacherAdmin> teacherid;
    public static volatile SingularAttribute<Appointmentmessage, Integer> id;
    public static volatile SingularAttribute<Appointmentmessage, String> message;

}