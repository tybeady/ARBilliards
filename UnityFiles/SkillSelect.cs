using UnityEngine;
using UnityEngine.SceneManagement;

//Last Update or Check: 01/23/20
public class SkillSelect : MonoBehaviour
{
    /*Create Skill Level Variable*/
    int skill_level;

    /*Camera & Cursor Components*/
    Vector3 cameraPos;

    /*Dimensions and Location of Buttons*/
    static float x = 250; 
    static float y = 160; 
    static int width = 150; //may change based on hololens view
    static int height = 100;

    /*Create Buttons*/
    Rect beginner = new Rect(x-160, y, width, height);
    Rect moderate = new Rect(x, y, width, height);
    Rect expert = new Rect(x+160, y, width, height);

    /*Data Streaming*/
    GameObject stream;

    private void Start()
    {
        stream = GameObject.FindGameObjectWithTag("SkillLevelSelect");
    }
    /*Note:
     * Find game object which contains ClientApplication.cs so you can call Post() from it.
     */

    private void Update()
    {
        cameraPos = Camera.main.transform.position;
        x = cameraPos.x;
        y = cameraPos.y;
    }
    /*Note:
     * We want to update our camera position constantly and assign the 
     * (x, y) location of our buttons to follow the positon of the camera.
     */

    void OnGUI()
    {
        GUI.Label(new Rect(x, y-50, width*3, 20), "Please Select Your Skill Level");

        if (GUI.Button(beginner, "Beginner"))
        {
            skill_level = 0;
            //Debug.Log(skill_level);
            stream.GetComponent<ClientApplication>().Post("SkillLevel", skill_level.ToString());
            SceneManager.LoadScene(sceneName: "Main");
        }
        if (GUI.Button(moderate, "Moderate"))
        {
            skill_level = 1;
            //Debug.Log(skill_level);
            stream.GetComponent<ClientApplication>().Post("SkillLevel", skill_level.ToString());
            SceneManager.LoadScene(sceneName: "Main");
        }
        if (GUI.Button(expert, "Expert"))
        {
            skill_level = 2;
            //Debug.Log(skill_level);
            stream.GetComponent<ClientApplication>().Post("SkillLevel", skill_level.ToString());
            SceneManager.LoadScene(sceneName: "Main");
        }
    }
    /*Note:
     * OnGUI() renders any specified GUI elements on the start of the script. 
     * Three clickable buttons render showing skill levels that the user may select.
     * Once button is clicked, skill_level is sent to server.
     */

}