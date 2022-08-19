package entities;

import entities.Roleinfo;
import entities.TeacherAdmin;
import java.util.Date;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:13")
@StaticMetamodel(News.class)
public class News_ { 

    public static volatile SingularAttribute<News, String> newstitle;
    public static volatile SingularAttribute<News, Integer> id;
    public static volatile SingularAttribute<News, Date> inputdate;
    public static volatile SingularAttribute<News, Roleinfo> forRole;
    public static volatile SingularAttribute<News, TeacherAdmin> teacherno;
    public static volatile SingularAttribute<News, String> content;

}