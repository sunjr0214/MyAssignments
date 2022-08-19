package entities;

import entities.Knowledge;
import entities.Parent;
import entities.Question;
import entities.Statusofresources;
import entities.Student;
import entities.TeacherAdmin;
import java.util.Date;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:14")
@StaticMetamodel(Reexamination.class)
public class Reexamination_ { 

    public static volatile SingularAttribute<Reexamination, Question> questionid;
    public static volatile SingularAttribute<Reexamination, Statusofresources> status2nd;
    public static volatile SingularAttribute<Reexamination, Parent> parentid;
    public static volatile SingularAttribute<Reexamination, Date> examinDate;
    public static volatile SingularAttribute<Reexamination, Knowledge> knowledgeid;
    public static volatile SingularAttribute<Reexamination, Student> studentid;
    public static volatile SingularAttribute<Reexamination, TeacherAdmin> toteacher;
    public static volatile SingularAttribute<Reexamination, Date> createdDate;
    public static volatile SingularAttribute<Reexamination, TeacherAdmin> teacherid;
    public static volatile SingularAttribute<Reexamination, Boolean> isCreate;
    public static volatile SingularAttribute<Reexamination, String> details;
    public static volatile SingularAttribute<Reexamination, Integer> id;
    public static volatile SingularAttribute<Reexamination, Statusofresources> status;

}