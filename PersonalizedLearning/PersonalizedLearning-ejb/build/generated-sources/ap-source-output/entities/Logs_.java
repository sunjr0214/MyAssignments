package entities;

import entities.Student;
import entities.TeacherAdmin;
import java.util.Date;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:14")
@StaticMetamodel(Logs.class)
public class Logs_ { 

    public static volatile SingularAttribute<Logs, Student> studentid;
    public static volatile SingularAttribute<Logs, String> recorderinfo;
    public static volatile SingularAttribute<Logs, TeacherAdmin> teacherid;
    public static volatile SingularAttribute<Logs, Integer> id;
    public static volatile SingularAttribute<Logs, String> tablename;
    public static volatile SingularAttribute<Logs, String> operation;
    public static volatile SingularAttribute<Logs, Date> operationtime;

}