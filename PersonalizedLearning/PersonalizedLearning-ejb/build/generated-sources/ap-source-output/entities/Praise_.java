package entities;

import entities.Knowledge;
import entities.Learningresource;
import entities.Question;
import entities.Student;
import java.util.Date;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:13")
@StaticMetamodel(Praise.class)
public class Praise_ { 

    public static volatile SingularAttribute<Praise, Knowledge> knowledgeId;
    public static volatile SingularAttribute<Praise, Student> studentId;
    public static volatile SingularAttribute<Praise, Date> praiseDate;
    public static volatile SingularAttribute<Praise, Question> questionId;
    public static volatile SingularAttribute<Praise, Integer> id;
    public static volatile SingularAttribute<Praise, Learningresource> learningresourceId;

}