package entities;

import entities.Question;
import entities.QuestionstudentcosttimePK;
import entities.Student;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(Questionstudentcosttime.class)
public class Questionstudentcosttime_ { 

    public static volatile SingularAttribute<Questionstudentcosttime, Integer> costtime;
    public static volatile SingularAttribute<Questionstudentcosttime, Question> question;
    public static volatile SingularAttribute<Questionstudentcosttime, QuestionstudentcosttimePK> questionstudentcosttimePK;
    public static volatile SingularAttribute<Questionstudentcosttime, Student> student;
    public static volatile SingularAttribute<Questionstudentcosttime, Integer> count;

}