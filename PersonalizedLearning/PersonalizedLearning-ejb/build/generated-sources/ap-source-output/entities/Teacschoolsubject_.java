package entities;

import entities.School;
import entities.Subject;
import entities.TeacherAdmin;
import java.util.Date;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:14")
@StaticMetamodel(Teacschoolsubject.class)
public class Teacschoolsubject_ { 

    public static volatile SingularAttribute<Teacschoolsubject, TeacherAdmin> teacherid;
    public static volatile SingularAttribute<Teacschoolsubject, School> schoolid;
    public static volatile SingularAttribute<Teacschoolsubject, Date> fromtime;
    public static volatile SingularAttribute<Teacschoolsubject, Integer> id;
    public static volatile SingularAttribute<Teacschoolsubject, Date> totime;
    public static volatile SingularAttribute<Teacschoolsubject, Subject> subjectid;

}