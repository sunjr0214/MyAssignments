package entities;

import entities.Studentdream;
import java.util.Date;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(Realizationofmydream.class)
public class Realizationofmydream_ { 

    public static volatile SingularAttribute<Realizationofmydream, Date> recorderdate;
    public static volatile SingularAttribute<Realizationofmydream, String> milestone;
    public static volatile SingularAttribute<Realizationofmydream, Studentdream> dreamid;
    public static volatile SingularAttribute<Realizationofmydream, Integer> id;

}