package entities;

import entities.Appointment;
import entities.Leadpoint;
import entities.Learningresource;
import entities.Logs;
import entities.PageColor;
import entities.Parent;
import entities.Praise;
import entities.Questionstudentcosttime;
import entities.Reexamination;
import entities.Roleinfo;
import entities.School;
import entities.Studentaccupoints;
import entities.Studentdream;
import entities.Studentschedule;
import entities.Studenttestpaper;
import entities.WrongquestionCollection;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(Student.class)
public class Student_ { 

    public static volatile SingularAttribute<Student, String> firstname;
    public static volatile SetAttribute<Student, Learningresource> learningresourceSet;
    public static volatile SetAttribute<Student, Studentdream> studentdreamCollection;
    public static volatile SetAttribute<Student, Leadpoint> leadpointSet;
    public static volatile SingularAttribute<Student, Parent> parentid;
    public static volatile SingularAttribute<Student, String> studentidinschool;
    public static volatile SingularAttribute<Student, String> password;
    public static volatile SingularAttribute<Student, School> schoolId;
    public static volatile SetAttribute<Student, Logs> logsSet;
    public static volatile SetAttribute<Student, Studenttestpaper> studenttestpaperSet;
    public static volatile SingularAttribute<Student, Integer> id;
    public static volatile SetAttribute<Student, Studentschedule> studentscheduleSet;
    public static volatile SetAttribute<Student, Reexamination> reexaminationCollection;
    public static volatile SingularAttribute<Student, String> email;
    public static volatile SingularAttribute<Student, String> thirdlogin;
    public static volatile SetAttribute<Student, PageColor> pageColorSet;
    public static volatile SetAttribute<Student, Praise> praiseSet;
    public static volatile SetAttribute<Student, WrongquestionCollection> wrongquestionCollectionSet;
    public static volatile SingularAttribute<Student, Roleinfo> roleId;
    public static volatile SingularAttribute<Student, String> secondname;
    public static volatile SetAttribute<Student, Appointment> appointmentSet;
    public static volatile SingularAttribute<Student, String> phone;
    public static volatile SingularAttribute<Student, String> name;
    public static volatile SetAttribute<Student, Questionstudentcosttime> questionstudentcosttimeSet;
    public static volatile SetAttribute<Student, Studentaccupoints> studentaccupointsSet;

}