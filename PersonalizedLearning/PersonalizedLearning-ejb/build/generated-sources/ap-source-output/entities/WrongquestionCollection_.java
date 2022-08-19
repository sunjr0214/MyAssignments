package entities;

import entities.Question;
import entities.Student;
import entities.WrongReason;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:13")
@StaticMetamodel(WrongquestionCollection.class)
public class WrongquestionCollection_ { 

    public static volatile SingularAttribute<WrongquestionCollection, Student> studentId;
    public static volatile SingularAttribute<WrongquestionCollection, Question> questionId;
    public static volatile SingularAttribute<WrongquestionCollection, WrongReason> reasonId;
    public static volatile SingularAttribute<WrongquestionCollection, Integer> id;

}