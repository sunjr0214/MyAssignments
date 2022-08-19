package entities;

import entities.School;
import entities.Studenttestpaper;
import entities.TeacherAdmin;
import java.util.Date;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:13")
@StaticMetamodel(Testpaper.class)
public class Testpaper_ { 

    public static volatile SingularAttribute<Testpaper, Integer> specifiedInterval;
    public static volatile SingularAttribute<Testpaper, String> subjectids;
    public static volatile SingularAttribute<Testpaper, Integer> degree;
    public static volatile SingularAttribute<Testpaper, Date> start;
    public static volatile SingularAttribute<Testpaper, Date> specifieddate;
    public static volatile SingularAttribute<Testpaper, Date> endtime;
    public static volatile SingularAttribute<Testpaper, TeacherAdmin> createteacherid;
    public static volatile SingularAttribute<Testpaper, Boolean> istest;
    public static volatile SingularAttribute<Testpaper, Integer> score;
    public static volatile SingularAttribute<Testpaper, School> schoolid;
    public static volatile SetAttribute<Testpaper, Studenttestpaper> studenttestpaperSet;
    public static volatile SingularAttribute<Testpaper, Integer> id;
    public static volatile SingularAttribute<Testpaper, Date> createDate;

}