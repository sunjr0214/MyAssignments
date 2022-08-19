package entities;

import entities.Student;
import entities.TeacherAdmin;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(PageColor.class)
public class PageColor_ { 

    public static volatile SingularAttribute<PageColor, TeacherAdmin> teacherId;
    public static volatile SingularAttribute<PageColor, Integer> rate;
    public static volatile SingularAttribute<PageColor, Integer> id;
    public static volatile SingularAttribute<PageColor, Student> userId;

}