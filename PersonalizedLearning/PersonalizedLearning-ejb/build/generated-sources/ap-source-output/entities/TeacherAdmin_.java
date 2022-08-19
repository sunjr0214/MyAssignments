package entities;

import entities.Appointmentmessage;
import entities.Learningresource;
import entities.Logs;
import entities.News;
import entities.PageColor;
import entities.Reexamination;
import entities.Roleinfo;
import entities.Studentaccupoints;
import entities.Teachermajor;
import entities.Teacherschedule;
import entities.Teacschoolsubject;
import entities.Testpaper;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:14")
@StaticMetamodel(TeacherAdmin.class)
public class TeacherAdmin_ { 

    public static volatile SingularAttribute<TeacherAdmin, String> thirdlogin;
    public static volatile SingularAttribute<TeacherAdmin, String> firstname;
    public static volatile SetAttribute<TeacherAdmin, PageColor> pageColorSet;
    public static volatile SingularAttribute<TeacherAdmin, Roleinfo> roleId;
    public static volatile SetAttribute<TeacherAdmin, News> newsSet;
    public static volatile SetAttribute<TeacherAdmin, Teacherschedule> teacherscheduleSet;
    public static volatile SetAttribute<TeacherAdmin, Learningresource> learningresourceSet;
    public static volatile SingularAttribute<TeacherAdmin, String> secondname;
    public static volatile SetAttribute<TeacherAdmin, Reexamination> reexaminationFromTeacher;
    public static volatile SingularAttribute<TeacherAdmin, String> password;
    public static volatile SetAttribute<TeacherAdmin, Testpaper> testpaperSet;
    public static volatile SingularAttribute<TeacherAdmin, String> phone;
    public static volatile SingularAttribute<TeacherAdmin, String> name;
    public static volatile SetAttribute<TeacherAdmin, Logs> logsSet;
    public static volatile SetAttribute<TeacherAdmin, Reexamination> reexaminationToTeacher;
    public static volatile SingularAttribute<TeacherAdmin, Integer> id;
    public static volatile SetAttribute<TeacherAdmin, Teachermajor> teachermajorSet;
    public static volatile SetAttribute<TeacherAdmin, Studentaccupoints> studentaccupointsSet;
    public static volatile SetAttribute<TeacherAdmin, Teacschoolsubject> teacschoolsubjectSet;
    public static volatile SingularAttribute<TeacherAdmin, String> email;
    public static volatile SetAttribute<TeacherAdmin, Appointmentmessage> appointmentmessageSet;

}