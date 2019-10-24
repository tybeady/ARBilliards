using UnityEngine;

public class Actions : MonoBehaviour
{
    //Misc. Variables
    Vector3[] tablePos = new Vector3[3];
    static float tableHeight; //we want to set this based off of getTablePos() & coordinate mapping
    int i = 0; //for getTablePos()
    bool tableExists = false;

    //Camera Components
    Vector3 cameraPos;

    //Target Line Positions 
    Vector3 cueStart = new Vector3(25, tableHeight, 35); //Set these based off of calculations script
    Vector3 cueEnd = new Vector3(35, tableHeight, 35);
    Vector3 objStart = new Vector3(35, tableHeight, 35);
    Vector3 objEnd = new Vector3(35, tableHeight, 40);

    //Colors, Materials, & Shaders
    string lineShader = "Mixed Reality Toolkit/Standard";
    Color lineColor = Color.blue;
    float lineWidth = 0.1f;

    void Start()
    {
        clearTablePos();
        //drawCueLine(cueStart, cueEnd);
        //drawObjLine(objStart, objEnd);
    }

    /****************************************************************************************************/

    bool validShot()
    {
        //Checks to see if cueStart/End and objStart/End are within table bounds.
        //Will we do this with image processing? If so, we won't need this.
        return true;
    }
    void drawCueLine(Vector3 cueStart, Vector3 cueEnd)
    {
        GameObject cueLine = new GameObject();
        cueLine.transform.position = cueStart;
        cueLine.AddComponent<LineRenderer>();
        LineRenderer clr = cueLine.GetComponent<LineRenderer>();
        clr.material = new Material(Shader.Find(lineShader));
        clr.material.color = lineColor;
        clr.startWidth = lineWidth;
        clr.endWidth = lineWidth;
        clr.SetPosition(0, cueStart);
        clr.SetPosition(1, cueEnd);
    }
    /* Note:
     * Draws the predicted trajectory line of the cue ball after hit with cue.
     */

    void drawObjLine(Vector3 objStart, Vector3 objEnd)
    {
        GameObject objLine = new GameObject();
        objLine.transform.position = objStart;
        objLine.AddComponent<LineRenderer>();
        LineRenderer olr = objLine.GetComponent<LineRenderer>();
        olr.material = new Material(Shader.Find(lineShader));
        olr.material.color = lineColor;
        olr.startWidth = lineWidth;
        olr.endWidth = lineWidth;
        olr.SetPosition(0, objStart);
        olr.SetPosition(1, objEnd);
    }
    /* Note:
     * Draws the predicted trajectory line of the object ball after hit with cue ball.
     */

    Vector3 getPoint()
    {
        cameraPos = Camera.main.gameObject.transform.position;
        //Debug.Log("getPoint at " + cameraPos.ToString());
        return cameraPos;
    }
    /* Note:
     * Grabs and returns the position of the spatial anchor.
     */

    void clearTablePos()
    {
        tablePos[0] = Vector3.zero;
        tablePos[1] = Vector3.zero;
        tablePos[2] = Vector3.zero;
    }
    /*Note:
     * Literally clears the position of the table.
     * Sets all table coordinates to zero. 
     */

    void getTablePos()
    {
        if (tablePos[2] == Vector3.zero)
        {
            while (i < 3)
            {
                tablePos[i] = getPoint();
                break;
            }
            i++;
            Debug.Log("tablePos:" + tablePos[0] + ", " + tablePos[1] + ", " + tablePos[2]);
        }
        else
        {
            //tableHeight = (tablePos[0].y+ tablePos[1].y+ tablePos[2].y)/3;
            tableHeight = 0f;
            if (tableExists == false)
            {
                //take this out eventually, it's just for testing...
                tablePos[0] = new Vector3(20, tableHeight, 30);
                tablePos[1] = new Vector3(50, tableHeight, 30);
                tablePos[2] = new Vector3(50, tableHeight, 80);
                //

                Debug.Log("Table position has been found!");
                setTablePos();
                tableExists = true;
            }
            else
            {
                Debug.Log("Table has already been drawn!");
            }  
        }
    }
    /*Note:
     * The point of this function is to determine the relative position of the pool table to the user
     * before they begin the game. 
     * First, check to see if the last tablePos entry is filled.
     * We want to iterate through the tablePos vector to fill each entry with an [x,y,x] coordinate.
     * This function waits to be called by a voice command.
     * Once all the entries of tablePos is filled, we use these coordinates to draw an imaginary 
     * boundary which sets the relative table position for the rest of the game?
     */

    void setTablePos()
    {
        Vector3 side1Start = new Vector3(tablePos[0].x, tableHeight, tablePos[0].z);
        Vector3 side1End = new Vector3(tablePos[1].x, tableHeight, tablePos[0].z);
        GameObject side1 = new GameObject();
        side1.transform.position = side1Start;
        side1.AddComponent<LineRenderer>();
        LineRenderer s1 = side1.GetComponent<LineRenderer>();
        s1.material = new Material(Shader.Find(lineShader));
        s1.material.color = Color.cyan;
        s1.startWidth = 1f;
        s1.endWidth = 1f;
        s1.SetPosition(0, side1Start);
        s1.SetPosition(1, side1End);

        Vector3 side2Start = new Vector3(tablePos[1].x, tableHeight, tablePos[0].z);
        Vector3 side2End = new Vector3(tablePos[1].x, tableHeight, tablePos[2].z);
        GameObject side2 = new GameObject();
        side2.transform.position = side2Start;
        side2.AddComponent<LineRenderer>();
        LineRenderer s2 = side2.GetComponent<LineRenderer>();
        s2.material = new Material(Shader.Find(lineShader));
        s2.material.color = Color.cyan;
        s2.startWidth = 1f;
        s2.endWidth = 1f;
        s2.SetPosition(0, side2Start);
        s2.SetPosition(1, side2End);

        Vector3 side3Start = new Vector3(tablePos[0].x, tableHeight, tablePos[2].z);
        Vector3 side3End = new Vector3(tablePos[1].x, tableHeight, tablePos[2].z);
        GameObject side3 = new GameObject();
        side3.transform.position = side3Start;
        side3.AddComponent<LineRenderer>();
        LineRenderer s3 = side3.GetComponent<LineRenderer>();
        s3.material = new Material(Shader.Find(lineShader));
        s3.material.color = Color.cyan;
        s3.startWidth = 1f;
        s3.endWidth = 1f;
        s3.SetPosition(0, side3Start);
        s3.SetPosition(1, side3End);

        Vector3 side4Start = new Vector3(tablePos[0].x, tableHeight, tablePos[0].z);
        Vector3 side4End = new Vector3(tablePos[0].x, tableHeight, tablePos[2].z);
        GameObject side4 = new GameObject();
        side4.transform.position = side2Start;
        side4.AddComponent<LineRenderer>();
        LineRenderer s4 = side4.GetComponent<LineRenderer>();
        s4.material = new Material(Shader.Find(lineShader));
        s4.material.color = Color.cyan;
        s4.startWidth = 1f;
        s4.endWidth = 1f;
        s4.SetPosition(0, side4Start);
        s4.SetPosition(1, side4End);
    }
    /* Note: Not complete (10/12)
     * Uses coordinates gathered from getTablePos() to actually draw the outline of the table.
     * This is a gross way to do this right now, so I'd like to clean this up.
     * We probably don't even need this, but here it is anyway.
     */

    private void OnMouseDown()
    {
        getTablePos();
        //GameObject.Destroy(object, elapsed_time);
    }
    /* Note: 
     * Simple button so I don't need to assign voice commands yet.
     */



}
