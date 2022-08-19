package entities;

import entities.Edgeamongsubject;
import entities.Knowledge;
import entities.Leadpoint;
import entities.Majorsubject;
import entities.Teacschoolsubject;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(Subject.class)
public class Subject_ { 

    public static volatile SetAttribute<Subject, Knowledge> knowledgeSet;
    public static volatile SetAttribute<Subject, Edgeamongsubject> edgeamongsubjectSet;
    public static volatile SetAttribute<Subject, Edgeamongsubject> edgeamongsubjectSet1;
    public static volatile SingularAttribute<Subject, String> name;
    public static volatile SingularAttribute<Subject, Integer> id;
    public static volatile SetAttribute<Subject, Majorsubject> majorsubjectSet;
    public static volatile SetAttribute<Subject, Teacschoolsubject> teacschoolsubjectSet;
    public static volatile SetAttribute<Subject, Leadpoint> leadpointSet;

}