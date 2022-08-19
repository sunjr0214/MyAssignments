package entities;

import entities.Edulevel;
import entities.Major;
import entities.School;
import entities.Student;
import entities.Teacschoolsubject;
import entities.Testpaper;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(School.class)
public class School_ { 

    public static volatile SingularAttribute<School, Edulevel> edulevel;
    public static volatile SetAttribute<School, Student> studentSet;
    public static volatile SingularAttribute<School, Major> majorid;
    public static volatile SetAttribute<School, Testpaper> testpaperSet;
    public static volatile SingularAttribute<School, String> name;
    public static volatile SingularAttribute<School, Integer> id;
    public static volatile SetAttribute<School, School> schoolSet;
    public static volatile SetAttribute<School, Teacschoolsubject> teacschoolsubjectSet;
    public static volatile SingularAttribute<School, School> parentid;

}