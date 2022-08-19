package entities;

import entities.Major;
import entities.Majorsubject;
import entities.School;
import entities.Teachermajor;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:14")
@StaticMetamodel(Major.class)
public class Major_ { 

    public static volatile SingularAttribute<Major, Major> parent;
    public static volatile SetAttribute<Major, Major> majorSet;
    public static volatile SingularAttribute<Major, String> name;
    public static volatile SingularAttribute<Major, Integer> id;
    public static volatile SetAttribute<Major, Teachermajor> teachermajorSet;
    public static volatile SetAttribute<Major, School> schoolSet;
    public static volatile SetAttribute<Major, Majorsubject> majorsubjectSet;

}