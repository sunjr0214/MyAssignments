package entities;

import entities.Student;
import entities.Studenttestpaper;
import entities.Subject;
import java.util.Date;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(Leadpoint.class)
public class Leadpoint_ { 

    public static volatile SingularAttribute<Leadpoint, String> knowledgeId;
    public static volatile SingularAttribute<Leadpoint, Student> studentId;
    public static volatile SetAttribute<Leadpoint, Studenttestpaper> studenttestpaperSet;
    public static volatile SingularAttribute<Leadpoint, Integer> id;
    public static volatile SingularAttribute<Leadpoint, Subject> subjectid;
    public static volatile SingularAttribute<Leadpoint, Date> createDate;

}