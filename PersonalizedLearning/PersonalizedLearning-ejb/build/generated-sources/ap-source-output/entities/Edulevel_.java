package entities;

import entities.School;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(Edulevel.class)
public class Edulevel_ { 

    public static volatile SingularAttribute<Edulevel, String> name;
    public static volatile SingularAttribute<Edulevel, Integer> id;
    public static volatile SetAttribute<Edulevel, School> schoolSet;

}