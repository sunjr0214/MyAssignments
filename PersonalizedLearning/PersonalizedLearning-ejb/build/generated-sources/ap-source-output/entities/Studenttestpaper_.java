package entities;

import entities.Leadpoint;
import entities.Student;
import entities.Testpaper;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:14")
@StaticMetamodel(Studenttestpaper.class)
public class Studenttestpaper_ { 

    public static volatile SingularAttribute<Studenttestpaper, String> firstWrongquestionids;
    public static volatile SingularAttribute<Studenttestpaper, Student> studentId;
    public static volatile SingularAttribute<Studenttestpaper, Integer> answeredInterval;
    public static volatile SingularAttribute<Studenttestpaper, Leadpoint> leadpointId;
    public static volatile SingularAttribute<Studenttestpaper, String> studentAnswer;
    public static volatile SingularAttribute<Studenttestpaper, Boolean> finished;
    public static volatile SingularAttribute<Studenttestpaper, Integer> id;
    public static volatile SingularAttribute<Studenttestpaper, String> questionIds;
    public static volatile SingularAttribute<Studenttestpaper, Double> testscore;
    public static volatile SingularAttribute<Studenttestpaper, String> otherwrongids;
    public static volatile SingularAttribute<Studenttestpaper, Testpaper> testpaperId;

}