package entities;

import entities.News;
import entities.Registeruser;
import entities.Student;
import entities.TeacherAdmin;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:14")
@StaticMetamodel(Roleinfo.class)
public class Roleinfo_ { 

    public static volatile SetAttribute<Roleinfo, Student> studentSet;
    public static volatile SetAttribute<Roleinfo, TeacherAdmin> teacherAdminSet;
    public static volatile SingularAttribute<Roleinfo, String> rolename;
    public static volatile SetAttribute<Roleinfo, News> newsSet;
    public static volatile SingularAttribute<Roleinfo, String> resources;
    public static volatile SetAttribute<Roleinfo, Registeruser> registeruserSet;
    public static volatile SingularAttribute<Roleinfo, Integer> id;

}