package entities;

import entities.Reexamination;
import entities.Roleinfo;
import entities.Student;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(Parent.class)
public class Parent_ { 

    public static volatile SingularAttribute<Parent, String> secondname;
    public static volatile SingularAttribute<Parent, String> thirdlogin;
    public static volatile SingularAttribute<Parent, String> password;
    public static volatile SingularAttribute<Parent, String> firstname;
    public static volatile SingularAttribute<Parent, String> phone;
    public static volatile SingularAttribute<Parent, Roleinfo> roleId;
    public static volatile SingularAttribute<Parent, String> name;
    public static volatile SetAttribute<Parent, Student> studentCollection;
    public static volatile SingularAttribute<Parent, Integer> id;
    public static volatile SetAttribute<Parent, Reexamination> reexaminationCollection;
    public static volatile SingularAttribute<Parent, String> email;

}