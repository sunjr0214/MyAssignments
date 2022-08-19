package entities;

import entities.Knowledge;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(Partofspeech.class)
public class Partofspeech_ { 

    public static volatile SingularAttribute<Partofspeech, String> chinese;
    public static volatile SetAttribute<Partofspeech, Knowledge> knowledgeSet;
    public static volatile SingularAttribute<Partofspeech, String> name;
    public static volatile SingularAttribute<Partofspeech, String> memo;
    public static volatile SingularAttribute<Partofspeech, Integer> id;

}