package entities;

import entities.Studentschedule;
import entities.Teacherschedule;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(Scheduleclass.class)
public class Scheduleclass_ { 

    public static volatile SingularAttribute<Scheduleclass, Boolean> donothingbeforefinish;
    public static volatile SingularAttribute<Scheduleclass, String> name;
    public static volatile SetAttribute<Scheduleclass, Teacherschedule> teacherscheduleSet;
    public static volatile SingularAttribute<Scheduleclass, Integer> id;
    public static volatile SetAttribute<Scheduleclass, Studentschedule> studentscheduleSet;

}