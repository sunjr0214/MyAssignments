package entities;

import entities.Edgeamongknowledge;
import entities.Learningresource;
import entities.Partofspeech;
import entities.Praise;
import entities.Question;
import entities.Reexamination;
import entities.Subject;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(Knowledge.class)
public class Knowledge_ { 

    public static volatile SetAttribute<Knowledge, Question> questionSet;
    public static volatile SetAttribute<Knowledge, Praise> praiseSet;
    public static volatile SetAttribute<Knowledge, Learningresource> learningresourceSet;
    public static volatile SetAttribute<Knowledge, Reexamination> reexaminationSet;
    public static volatile SingularAttribute<Knowledge, String> c1;
    public static volatile SingularAttribute<Knowledge, Integer> praiseCnt;
    public static volatile SingularAttribute<Knowledge, Subject> subjectId;
    public static volatile SingularAttribute<Knowledge, String> c2;
    public static volatile SetAttribute<Knowledge, Edgeamongknowledge> edgeamongknowledgeSet;
    public static volatile SingularAttribute<Knowledge, String> c3;
    public static volatile SingularAttribute<Knowledge, Partofspeech> c4;
    public static volatile SingularAttribute<Knowledge, String> c5;
    public static volatile SetAttribute<Knowledge, Edgeamongknowledge> edgeamongknowledgeSet1;
    public static volatile SingularAttribute<Knowledge, String> name;
    public static volatile SingularAttribute<Knowledge, String> details;
    public static volatile SingularAttribute<Knowledge, Integer> id;
    public static volatile SingularAttribute<Knowledge, Integer> levelnumber;

}