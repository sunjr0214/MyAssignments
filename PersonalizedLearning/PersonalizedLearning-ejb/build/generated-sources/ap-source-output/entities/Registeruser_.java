package entities;

import entities.Roleinfo;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(Registeruser.class)
public class Registeruser_ { 

    public static volatile SingularAttribute<Registeruser, String> secondname;
    public static volatile SingularAttribute<Registeruser, String> password;
    public static volatile SingularAttribute<Registeruser, String> firstname;
    public static volatile SingularAttribute<Registeruser, Roleinfo> roleid;
    public static volatile SingularAttribute<Registeruser, String> name;
    public static volatile SingularAttribute<Registeruser, Integer> id;
    public static volatile SingularAttribute<Registeruser, String> email;

}