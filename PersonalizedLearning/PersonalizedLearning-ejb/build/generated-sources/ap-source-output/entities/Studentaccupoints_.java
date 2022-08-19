package entities;

import entities.Student;
import entities.TeacherAdmin;
import java.util.Date;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(Studentaccupoints.class)
public class Studentaccupoints_ { 

    public static volatile SingularAttribute<Studentaccupoints, Student> studentId;
    public static volatile SingularAttribute<Studentaccupoints, String> reason;
    public static volatile SingularAttribute<Studentaccupoints, TeacherAdmin> teacherId;
    public static volatile SingularAttribute<Studentaccupoints, Date> modifyDate;
    public static volatile SingularAttribute<Studentaccupoints, Integer> id;
    public static volatile SingularAttribute<Studentaccupoints, Double> pointsNum;

}