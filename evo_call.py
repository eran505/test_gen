
import glob, os



def assemble_path_string2(str) :
    print str
    cutoff = 0
    suffix=""
    prefix=""
    len_str = len(str)
    word =''
    for i in range(len_str-1, 0, -1) :
        cutoff += 1
        if str[i]=='/' :
            word_r = reversed(word)
            word = ''.join(word_r)
            if word == 'classes':
                prefix = str[0:len_str - cutoff + len(word)+1]
                break
            suffix=word+"."+suffix
            word = ""
        else :
            word=word+str[i]
    print prefix
    print suffix
    return prefix,suffix


def get_all_class(root) :
    size=0
    class_list = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            #print os.path.join(path, name)
            if name.__contains__("$") is False:
                size+=1
                class_list.append([str(path),str(name)])
    print "size=",size
    return class_list


def single_call_EvoSuite(evo_name,evo_path,classes_list,time,dis_path):

    evo_string = "java -jar " + evo_path +evo_name


    parms1="-Dsearch_budget="+time
    parms2=" -Dglobal_timeout="+time
    parms3=" -Dreport_dir="+dis_path
    parms4=" -Dtest_dir="+dis_path

    all_p = parms1+parms2+parms2+parms3+parms4

    for cut in classes_list :
        cut_names = str(cut[1]).split('.')
        pre,suf = assemble_path_string2(cut[0])
        test = suf  + cut_names[0]
        command = evo_string + " -class " +test+" -projectCP "+pre+" "+all_p
        print command
        os.system(command)
        break




path_1 = "/home/eran/thesis/Tutorial/Tutorial_Experiments/target/classes/tutorial/"

path_2 = "/home/eran/thesis/projects-ex/commons-math3-3.6.1-src/target/classes/org/"

evo_path="/home/eran/programs/EVOSUITE/jar/"

evo_name = "evosuite-1.0.4.jar"

evo_name_sanpshot = "evosuite-master-1.0.6-SNAPSHOT.jar"

evo_st_name ="evosuite-standalone-runtime-1.0.4.jar"

dis_path = "/home/eran/Desktop/evo_result/"

target_list = get_all_class(path_2)

single_call_EvoSuite(evo_name_sanpshot,evo_path,target_list,'5',dis_path)
