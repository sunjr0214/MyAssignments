package entities;

import entities.Realizationofmydream;
import entities.Student;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:13")
@StaticMetamodel(Studentdream.class)
public class Studentdream_ { 

    public static volatile SingularAttribute<Studentdream, Student> stuid;
    public static volatile SingularAttribute<Studentdream, Integer> id;
    public static volatile SingularAttribute<Studentdream, String> media;
    public static volatile SingularAttribute<Studentdream, String> title;
    public static volatile SingularAttribute<Studentdream, String> plan;
    public static volatile SingularAttribute<Studentdream, String> knowledges;
    public static volatile SetAttribute<Studentdream, Realizationofmydream> realizationofmydreamCollection;
    public static volatile SingularAttribute<Studentdream, String> mydream;

}