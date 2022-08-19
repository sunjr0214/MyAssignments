package entities;

import entities.Edgeamongknowledge;
import entities.Knowledge;
import entities.Praise;
import entities.Student;
import entities.TeacherAdmin;
import java.util.Date;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:14")
@StaticMetamodel(Learningresource.class)
public class Learningresource_ { 

    public static volatile SingularAttribute<Learningresource, Knowledge> knowledgeId;
    public static volatile SingularAttribute<Learningresource, Student> studentId;
    public static volatile SingularAttribute<Learningresource, Boolean> isPassed;
    public static volatile SingularAttribute<Learningresource, Date> createdDate;
    public static volatile SingularAttribute<Learningresource, TeacherAdmin> teacherId;
    public static volatile SetAttribute<Learningresource, Praise> praiseSet;
    public static volatile SingularAttribute<Learningresource, Edgeamongknowledge> edgeamongKnowledgeId;
    public static volatile SingularAttribute<Learningresource, String> valueinfo;
    public static volatile SingularAttribute<Learningresource, Integer> id;
    public static volatile SingularAttribute<Learningresource, Integer> type;
    public static volatile SingularAttribute<Learningresource, Integer> praiseCnt;

}